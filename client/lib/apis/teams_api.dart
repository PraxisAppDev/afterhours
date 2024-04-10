import 'dart:convert';

import 'package:json_annotation/json_annotation.dart';
import 'package:http/http.dart';
import 'package:praxis_afterhours/reusables/hunt_structure.dart' hide Response;

import 'api_client.dart';
import 'api_utils/token.dart';
import 'api_utils/stream_request.dart';

part 'teams_api.g.dart';

@JsonSerializable()
class TeamsResponseModel {
  final String message;
  final List<Team> content;

  TeamsResponseModel({
    required this.message,
    required this.content,
  });

  factory TeamsResponseModel.fromJson(Map<String, dynamic> json) => _$TeamsResponseModelFromJson(json);

  Map<String, dynamic> toJson() => _$TeamsResponseModelToJson(this);
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

Stream<List<Team>> watchListTeams(String huntId) async* {
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  yield* StreamRequest.get(
    Uri.parse("$apiUrl/game/$huntId/teams/list_teams"),
    headers: {
      "authorization": "Bearer $token"
    },
    converter: (json) => (json as List<Object?>)
        .map((e) => Team.fromJson(e as Map<String, dynamic>))
        .toList(),
  ).send(client);
}

Future<Team> createTeam(String huntId, String teamName) async {
  Response response;
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  try {
    response = await client.post(Uri.parse("$apiUrl/game/$huntId/teams/create_team"),
        headers: {
          "authorization": "Bearer $token",
          "Content-Type": "application/json"
        },
        body: jsonEncode({"name": teamName})
    );
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 201) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return Team.fromJson(jsonResponse);
  } else {
    throw Exception("Error: Failed to create team: $response.statusCode");
  }
}

Future<List<Player>> getListPlayersForTeam(String huntId, String teamId) async {
  Response response;
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  try {
    response = await client.get(Uri.parse("$apiUrl/game/$huntId/teams/$teamId/members"),
        headers: {
          "authorization": "Bearer $token"
        }
    );
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body) as List<dynamic>;
    return jsonResponse.map((e) => Player.fromJson(e as Map<String, dynamic>)).toList();
  } else {
    throw Exception("Error: Failed to load players: $response.statusCode");
  }
}

Stream<List<Player>> watchListPlayersForTeam(String huntId, String teamId) async* {
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  yield* StreamRequest.get(
    Uri.parse("$apiUrl/game/$huntId/teams/$teamId/listen_members"),
    headers: {
      "authorization": "Bearer $token"
    },
    converter: (json) => (json as List<Object?>)
        .map((e) => Player.fromJson(e as Map<String, dynamic>))
        .toList(),
  ).send(client);
}

Future<List<String>> getListJoinRequestsForTeam(String huntId, String teamId) async {
  Response response;
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  try {
    response = await client.get(Uri.parse("$apiUrl/game/$huntId/teams/$teamId/join_requests"),
        headers: {
          "authorization": "Bearer $token"
        }
    );
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body) as List<dynamic>;
    return jsonResponse.cast<String>().toList();
  } else {
    throw Exception("Error: Failed to load join requests: $response.statusCode");
  }
}

Stream<List<String>> watchListJoinRequestsForTeam(String huntId, String teamId) async* {
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  yield* StreamRequest.get(
    Uri.parse("$apiUrl/game/$huntId/teams/$teamId/listen_join_requests"),
    headers: {
      "authorization": "Bearer $token"
    },
    converter: (json) => (json as List<Object?>)
        .cast<String>()
        .toList(),
  ).send(client);
}

@JsonSerializable()
class TeamOperationSuccessMessage {
  final String message;

  TeamOperationSuccessMessage({
    required this.message,
  });

  factory TeamOperationSuccessMessage.fromJson(Map<String, dynamic> json) => _$TeamOperationSuccessMessageFromJson(json);

  Map<String, dynamic> toJson() => _$TeamOperationSuccessMessageToJson(this);
}

Future<TeamOperationSuccessMessage> requestJoinTeam(String huntId, String teamId) async {
  Response response;
  String? token = await getToken();
  if(token == null) throw Exception("User is not logged in.");
  try {
    response = await client.post(Uri.parse("$apiUrl/game/$huntId/teams/$teamId/request_join"),
        headers: {
          "authorization": "Bearer $token",
          "Content-Type": "application/json"
        }
    );
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 201) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return TeamOperationSuccessMessage.fromJson(jsonResponse);
  } else {
    throw Exception("Error: Failed to request to join team: $response.statusCode");
  }
}

Future<TeamOperationSuccessMessage> cancelRequestJoinTeam(
    String huntId, String teamId) async {
  Response response;
  String? token = await getToken();
  if (token == null) throw Exception("User is not logged in.");
  try {
    response = await client.post(
        Uri.parse("$apiUrl/game/$huntId/teams/$teamId/cancel_request_join"),
        headers: {
          "authorization": "Bearer $token",
          "Content-Type": "application/json"
        });
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 201) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return TeamOperationSuccessMessage.fromJson(jsonResponse);
  } else {
    throw Exception(
        "Error: Failed to cancel request to join team: ${response.statusCode}");
  }
}

Future<TeamOperationSuccessMessage> acceptRequestJoinTeam(
    String huntId, String teamId, String playerId) async {
  Response response;
  String? token = await getToken();
  if (token == null) throw Exception("User is not logged in.");
  try {
    response = await client.post(
        Uri.parse("$apiUrl/game/$huntId/teams/$teamId/join_requests/$playerId/accept"),
        headers: {
          "authorization": "Bearer $token",
          "Content-Type": "application/json"
        },
        body: jsonEncode({"player_id": playerId}));
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 201) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return TeamOperationSuccessMessage.fromJson(jsonResponse);
  } else {
    throw Exception(
        "Error: Failed to accept request to join team: ${response.statusCode}");
  }
}

Future<TeamOperationSuccessMessage> rejectRequestJoinTeam(
    String huntId, String teamId, String playerId) async {
  Response response;
  String? token = await getToken();
  if (token == null) throw Exception("User is not logged in.");
  try {
    response = await client.delete(
        Uri.parse("$apiUrl/game/$huntId/teams/$teamId/join_requests/$playerId"),
        headers: {
          "authorization": "Bearer $token",
          "Content-Type": "application/json"
        },
        body: jsonEncode({"player_id": playerId}));
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 201) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return TeamOperationSuccessMessage.fromJson(jsonResponse);
  } else {
    throw Exception(
        "Error: Failed to reject request to join team: ${response.statusCode}");
  }
}

Future<void> removeMember(String huntId, String teamId, String memberId) async {
  Response response;
  String? token = await getToken();
  if (token == null) throw Exception("User is not logged in.");
  try {
    response = await client.delete(
        Uri.parse("$apiUrl/game/$huntId/teams/$teamId/members/$memberId"),
        headers: {
          "authorization": "Bearer $token",
        });
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode != 200) {
    throw Exception(
        "Error: Failed to remove member from team: ${response.statusCode}");
  }
}