import 'package:flutter/material.dart';
import 'package:praxis_afterhours/views/splash.dart';
import 'package:praxis_afterhours/views/hunt_challenge_screen.dart';

void main() {
  runApp(
    MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        fontFamily: "Poppins",
      ),
      home: HuntChallengeScreen(),
    ),
  );
}
