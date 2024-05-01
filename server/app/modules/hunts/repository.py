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
        "$gte": date.isoformat()
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
            challenge["score"] = current_challenge_attempt.get("pointsIfCorrect") + team[0]["score"]
            # team[0]["score"] = challenge.get("score")
          challenge_return = [challenge for challenge in team_challenge_results_list if challenge["challengeId"] == current_challenge_attempt.get("challengeId")]
          
          team[0]["challengeResults"] = team_challenge_results_list
          team[0]["score"] = challenge.get("score")
          new_teams_list= [team for team in list_teams if team.get("id") != id_team]
          new_teams_list.append(team[0])
          result = await self.collection.update_one({"_id": ObjectId(hunt_id)}, {"$set": {"gameState": {"teams": new_teams_list}}})
          return challenge_return[0]
        
      if solved_boolean == True:
        challenge_result_model = {"challengeId":current_challenge_attempt.get("challengeId"), "solved":solved_boolean, "elapsedTime":current_challenge_attempt.get("elapsedTime"), "answerAttempts":current_challenge_attempt.get("answerAttempts"), "score":current_challenge_attempt.get("pointsIfCorrect") + team[0]["score"]}
      else:
        challenge_result_model = {"challengeId":current_challenge_attempt.get("challengeId"), "solved":solved_boolean, "elapsedTime":current_challenge_attempt.get("elapsedTime"), "answerAttempts":current_challenge_attempt.get("answerAttempts"), "score":team[0]["score"]}
  
      team[0]["challengeResults"].append(challenge_result_model)
      if solved_boolean == True:
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
    
    elif (response.get("type") == "number"):
      possible_Answers_List = response.get("possibleAnswers")

      for correct_answer in possible_Answers_List:
        if correct_answer == int(challenge_attempt.get("answerProvided")):
          solved = True
          return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
    
    elif (response.get("type") == "string_set_matched"):
      attempt_list = challenge_attempt.get("answerProvided").split(",")
      attempt_list = [x.strip() for x in attempt_list]

      #IMPORTANT: This is harcoded to be 3. When schema is changed to allow numOfAnswers, change to len(set(attempt_list))!=response.get("numOfAnswers")
      if(len(set(attempt_list))!=3):
        solved = False
        return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
      
      possible_answers_list = response.get("possibleAnswers")
      solved = True
      
      for attempt in attempt_list:
        if(response.get("caseSensitive") == True):
          if(attempt not in possible_answers_list):
            solved = False
            return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
        else:
          case_possible_answers_list = [x.casefold() for x in possible_answers_list]
          if(attempt.casefold().strip() not in case_possible_answers_list):
            solved = False
            return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
      return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
    
    elif (response.get("type") == "multiple_choice"):
      correct_answer = response.get("correctAnswers")
      
      for answer_index in correct_answer:
        if (response.get("choices")[answer_index]).casefold().strip() == challenge_attempt.get("answerProvided").casefold().strip():
            solved = True
            return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
    
    elif(response.get("type") == "number_range"):
      min = response.get("minAnswer")
      max = response.get("maxAnswer")
      attempt = int(challenge_attempt.get("answerProvided"))

      if(min<=attempt and max>=attempt):
        solved = True
        return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
    
    elif(response.get("type") == "date_time"):
      #for min and max, datetime has the format 2023-09-11
      min = datetime.strptime(response.get("minAnswer"), '%Y-%m-%dT%H:%M:%S').date()
      max = datetime.strptime(response.get("maxAnswer"), '%Y-%m-%dT%H:%M:%S').date()
      #datetime is set to have the format 09-11-2023 for users to input. 
      attempt = datetime.strptime(challenge_attempt.get("answerProvided"), '%m-%d-%Y').date()

      if(min<=attempt and max>=attempt):
        solved = True
        return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
    
    elif(response.get("type") == "qr_code_id_response"):
      #AI TAKES OVER (RAAAAAAA!!!)
      solved = False


    solved = False
    return await update_team_challenge_result(solved, team_challenge_results, challenge_attempt, teams_list, id_hunt, team_id)
            

repository = HuntRepository()
