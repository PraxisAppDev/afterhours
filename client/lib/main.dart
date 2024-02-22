import 'package:flutter/material.dart';
import 'package:praxis_afterhours/views/splash.dart';

void main() {
  runApp(
    MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        fontFamily: "Poppins",
      ),
      home: const Splash(),
    ),
  );
}
