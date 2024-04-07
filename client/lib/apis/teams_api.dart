import 'dart:convert';

import 'package:json_annotation/json_annotation.dart';
import 'package:http/http.dart';

import 'api_client.dart';
import 'api_utils/token.dart';
import 'api_utils/stream_request.dart';

part 'teams_api.g.dart';

@JsonSerializable()
class TeamsResponseModel {
  final String message;
  final List<TeamModel> teams;

  TeamsResponseModel({
    required this.message,
    required this.teams,
  });

  factory TeamsResponseModel.fromJson(Map<String, dynamic> json) => _$TeamsResponseModelFromJson(json);

  Map<String, dynamic> toJson() => _$TeamsResponseModelToJson(this);
}

@JsonSerializable()
class TeamModel {
  @JsonKey(name: "hunt_id")
  final String huntId;
  @JsonKey(name: "name")
  final String teamName;
  final String teamLead;
  final List<String> playerIds;
  final List<String> challengeResults;
  final List<String> invitations;

  TeamModel({
    required this.huntId,
    required this.teamName,
    required this.teamLead,
    required this.playerIds,
    required this.challengeResults,
    required this.invitations,
  });

  factory TeamModel.fromJson(Map<String, dynamic> json) => _$TeamModelFromJson(json);
  Map<String, dynamic> toJson() => _$TeamModelToJson(this);
}


Future<TeamsResponseModel> listTeams(String huntId) async {
  Response response;
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  try {
    response = await client.get(Uri.parse("$apiUrl/game/$huntId/teams/list_teams"),
        headers: {
          "authorization": "Bearer $token"
        }
    );
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return TeamsResponseModel.fromJson(jsonResponse);
  } else {
    throw Exception("Error: Failed to load teams: $response.statusCode");
  }
}

Stream<List<TeamModel>> watchListTeams(String huntId) async* {
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  yield* StreamRequest.get(
    Uri.parse("$apiUrl/game/$huntId/teams/list_teams"),
    headers: {
      "authorization": "Bearer $token"
    },
    converter: (json) => (json as List<Object?>)
        .map((e) => TeamModel.fromJson(e as Map<String, dynamic>))
        .toList(),
  ).send(client);
}