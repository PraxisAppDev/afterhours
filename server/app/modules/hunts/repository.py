from app.database import database
from app.modules.hunts.router_models import ChallengeModel
from app.modules.hunts.hunt_models import ChallengeAttempt, ChallengeResult
from app.util import handle_object_id
from datetime import datetime
from bson import ObjectId
from typing import List
from app.modules.game.teams.router_models import Team
import json


class HuntRepository:
  def __init__(self):
    self.collection = database.get_collection("hunts")
  
  async def get_all_past_date(self, date=datetime.now()):
    cursor = self.collection.find({
      "endDate": {
        "$gte": date.strftime("%Y-%m-%d %I:%M %p")
      }
    })
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))

  async def get_all_before_date(self, date=datetime.now()):
    cursor = self.collection.find({
      "endDate": {
        "$lt": date
      }
    })
    cursor = cursor.listens_to()  # TODO: probably have to remove this line
    return list(map(lambda document: handle_object_id(document), await cursor.to_list(1000)))

  async def create_hunt(self, hunt_document: ChallengeModel):
    result = await self.collection.insert_one(json.loads(hunt_document.json()))
    if result:
      return str(result.inserted_id)

  async def check_answer(self, id_hunt: str, team_id: str, challenge_attempt: ChallengeAttempt):
    hunt = await self.collection.find_one({"_id": ObjectId(id_hunt)})
    challenges_array = hunt.get("challenges")
    challenge_attempt = json.loads(challenge_attempt.model_dump_json())

    challenge = [challenge for challenge in challenges_array if challenge.get("id") == challenge_attempt.get("challengeId")]
    response = challenge[0].get("response")

    teams_list = hunt.get("gameState").get("teams")
    team = [team for team in teams_list if team.get("id") == team_id]
    team[0]["challengeAttempts"].append(challenge_attempt)
    team_challenge_results = team[0].get("challengeResults")

    async def update_team_challenge_result(solved_boolean: bool, team_challenge_results_list: List[ChallengeResult], current_challenge_attempt: ChallengeAttempt, list_teams: List[Team], hunt_id: str, id_team: str):
      team = [team for team in list_teams if team.get("id") == id_team]
      for challenge in team_challenge_results_list:
        if challenge["challengeId"] == current_challenge_attempt.get("challengeId"):
          challenge["solved"] = solved_boolean
          challenge["elapsedTime"] = current_challenge_attempt.get("elapsedTime")
          challenge["answerAttempts"] = current_challenge_attempt.get("answerAttempts")
          if solved_boolean == True:
            challenge["score"] = current_challenge_attempt.get("pointsAwarded") + challenge.get("score")
          challenge_return = [challenge for challenge in team_challenge_results_list if challenge["challengeId"] == current_challenge_attempt.get("challengeId")]
          
          team[0]["challengeResults"] = team_challenge_results_list
          team[0]["score"] = challenge.get("score")
          new_teams_list= [team for team in list_teams if team.get("id") != id_team]
          new_teams_list.append(team[0])
          result = await self.collection.update_one({"_id": ObjectId(hunt_id)}, {"$set": {"gameState": {"teams": new_teams_list}}})
          return challenge_return[0]
        
      if solved_boolean == True:
        challenge_result_model = {"challengeId":current_challenge_attempt.get("challengeId"), "solved":solved_boolean, "elapsedTime":current_challenge_attempt.get("elapsedTime"), "answerAttempts":current_challenge_attempt.get("answerAttempts"), "score":current_challenge_attempt.get("pointsAwarded")}
      else:
        challenge_result_model = {"challengeId":current_challenge_attempt.get("challengeId"), "solved":solved_boolean, "elapsedTime":current_challenge_attempt.get("elapsedTime"), "answerAttempts":current_challenge_attempt.get("answerAttempts"), "score":0.0}
  
      team[0]["challengeResults"].append(challenge_result_model)
      team[0]["score"] = challenge_result_model.get("score")
      new_teams_list= [team for team in list_teams if team.get("id") != id_team]
      new_teams_list.append(team[0])
      result = await self.collection.update_one({"_id": ObjectId(hunt_id)}, {"$set": {"gameState": {"teams": new_teams_list}}})
      if result:
        return challenge_result_model

    if (response.get("type") == "string_text_field"):
      possible_Answers_List = response.get("possibleAnswers")
      for correct_answer in possible_Answers_List:
        if (response.get("caseSensitive") == True):
          if correct_answer == challenge_attempt.get("answerProvided"):

            solved = True
            return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
        else:
          if correct_answer.casefold() == challenge_attempt.get("answerProvided").casefold():
            solved = True
            return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
          
      solved = False
      return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
            

repository = HuntRepository()
