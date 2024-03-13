import 'dart:convert';
import 'package:http/http.dart';
import 'package:praxis_afterhours/apis/api_client.dart';
import 'package:praxis_afterhours/storage/secure_storage.dart';

// TODO: refactor into own component to be used for everyone
Future<String?> getToken() async {
  try {
    final token = await storage.read(key: "token");
    return token;
  } catch (e) {
    throw Exception("Failed to read token");
  }
}

Future<Map<String, dynamic>> fetchUserInfo() async {
  final token = await getToken();
  Response response;

  try {
    response = await client.get(Uri.parse("$apiUrl/users/get_user_info"),
        headers: {
          "content-type": "application/json",
          "authorization": "Bearer $token"
        });
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 200) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return jsonResponse;
  } else {
    throw Exception("Failed to load user data: $response.statusCode");
  }
}

Future<void> updateUserInfo(Map<dynamic, dynamic> userInfo) async {
  final token = await getToken();
  Response response;

  try {
    response = await client.put(Uri.parse("$apiUrl/users/update_user_info"),
        headers: {
          "content-type": "application/json",
          "authorization": "Bearer $token"
        },
        body: jsonEncode(userInfo));
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 200) {
    // User info updated successfully
  } else {
    throw Exception("Failed to update user info: ${response.statusCode}");
  }
}
