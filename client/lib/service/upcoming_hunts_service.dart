import 'dart:convert';
import 'package:praxis_afterhours/entities/upcoming_hunt.dart';
import 'package:http/http.dart' as http;

List<UpcomingHunt> parseUpcomingHunts(String responseBody) {
  final parsed =
      (jsonDecode(responseBody) as List).cast<Map<String, dynamic>>();

  return parsed
      .map<UpcomingHunt>((json) => UpcomingHunt.fromJson(json))
      .toList();
}

Future<List<UpcomingHunt>> fetchUpcomingHunts() async {
  final response = await http.get(
    Uri.parse("http://localhost:8001/hunts/upcoming"),
  );

  if (response.statusCode == 200) {
    return parseUpcomingHunts(response.body);
  } else {
    throw Exception("Failed to load upcoming hunts");
  }
}
