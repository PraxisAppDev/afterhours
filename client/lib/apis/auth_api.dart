import 'dart:convert';
import 'package:http/http.dart';
import 'package:praxis_afterhours/apis/api_client.dart';

Future<String> logIn(String username, String password) async {
  Response response;
  try {
    response = await client.post(Uri.parse("$apiUrl/users/auth/login"),
        headers: {"content-type": "application/json"},
        body: jsonEncode({"username": username, "password": password}));
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 201) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return jsonResponse["token"]["access_token"];
  } else {
    throw const FormatException("invalid credentials");
  }
}

Future<String> signUp(
    String username, String email, String fullname, String password) async {
  Response response;
  try {
    response = await client.post(Uri.parse("$apiUrl/users/auth/signup"),
        headers: {"content-type": "application/json"},
        body: jsonEncode({
          "username": username,
          "email": email,
          "fullname": fullname,
          "password": password
        }));
  } catch (error) {
    throw Exception("network error");
  }
  if (response.statusCode == 201) {
    var jsonResponse = jsonDecode(response.body) as Map<String, dynamic>;
    return jsonResponse["token"]["access_token"];
  } else {
    throw const FormatException("invalid credentials");
  }
}