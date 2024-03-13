import 'dart:convert';
import 'package:praxis_afterhours/entities/team.dart';
import 'package:http/http.dart' as http;

List<Team> parseTeams(String responseBody) {
  final parsed =
      (jsonDecode(responseBody) as List).cast<Map<String, dynamic>>();

  return parsed.map<Team>((json) => Team.fromJson(json)).toList();
}

Future<List<Team>> fetchTeams() async {
  final response = await http.get(
    Uri.parse("http://localhost:8001/hunts/teams/get_team_info"),
  );

  if (response.statusCode == 200) {
    return parseTeams(response.body);
  } else {
    throw Exception("Failed to load available teams: service");
  }
}
