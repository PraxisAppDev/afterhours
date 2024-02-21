import 'package:flutter/material.dart';
import 'package:praxis_afterhours/views/sign_in_view.dart';

void main() {
  runApp(
    MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        fontFamily: "Poppins",
      ),
      home: SignInView(),
    ),
  );
}
