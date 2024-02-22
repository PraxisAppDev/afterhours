import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';
import 'package:praxis_afterhours/app_utils/basic_text_field.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/views/bottom_nav_bar.dart';
import 'package:praxis_afterhours/views/create_account_view.dart';

class SignInView extends StatelessWidget {
  SignInView({super.key});

  final _formKey = GlobalKey<FormState>();

  String error = "";

  TextEditingController emailController = TextEditingController();
  TextEditingController passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        //Setting the margins of the content of the view.
        margin: const EdgeInsets.only(
          left: 24.0,
          right: 24.0,
          top: 100,
          bottom: 50,
        ),
        //Column holding the content of the view
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // "Sign In" and "Welcome back."
              Container(
                alignment: Alignment.centerLeft,
                child: const Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      "Sign In",
                      style: TextStyle(
                        fontSize: 35,
                        fontWeight: FontWeight.normal,
                        color: praxisBlack,
                      ),
                    ),
                    Text(
                      "Welcome back.",
                      style: TextStyle(
                        fontSize: 20,
                        fontWeight: FontWeight.w100,
                        color: praxisBlack,
                      ),
                    ),
                  ],
                ),
              ),
              //Email Address
              BasicTextField(
                labelText: "Email Address",
                fieldType: BasicTextFieldType.email,
                editingController: emailController,
                validatorError: "Please enter your email",
              ),
              //Password
              BasicTextField(
                labelText: "Password",
                // To disable the password requirement
                fieldType: BasicTextFieldType.custom,
                editingController: passwordController,
                validatorError: "Please enter your password",
                obscureText: true,
              ),
              //Forgot Password
              Container(
                alignment: Alignment.topRight,
                child: TextButton(
                  onPressed: () {},
                  child: const Text(
                    "Forgot Password?",
                    style: TextStyle(
                      color: praxisBlack,
                      fontSize: 12,
                      fontWeight: FontWeight.w100,
                      decoration: TextDecoration.underline,
                      decorationColor: praxisBlack,
                    ),
                  ),
                ),
              ),
              //Log In
              Container(
                decoration: const BoxDecoration(
                  color: praxisRed,
                  borderRadius: BorderRadius.all(Radius.circular(5)),
                ),
                child: TextButton(
                  onPressed: () async {
                    if (_formKey.currentState!.validate()) {
                      // print("All fields valid.");
                      Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const BottomNavBar(),
                        ),
                      );
                      //insert sign-in logic here
                    }
                  },
                  child: const Text(
                    "Log In",
                    style: TextStyle(
                      color: praxisWhite,
                    ),
                  ),
                ),
              ),
              //Divider (----or-----)
              Row(
                children: [
                  Expanded(
                    child: Container(
                      margin: const EdgeInsets.only(right: 10),
                      child: const Divider(color: praxisBlack),
                    ),
                  ),
                  const Text(
                    "or",
                    style: TextStyle(
                      color: praxisBlack,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  Expanded(
                    child: Container(
                      margin: const EdgeInsets.only(left: 10),
                      child: const Divider(color: praxisBlack),
                    ),
                  ),
                ],
              ),
              //Sign In with Facebook
              Container(
                decoration: const BoxDecoration(
                  color: Color(0xFF125EEE),
                  borderRadius: BorderRadius.all(Radius.circular(5)),
                ),
                child: TextButton(
                  onPressed: () {},
                  child: Row(
                    children: [
                      Padding(
                        padding: const EdgeInsets.only(left: 8.0),
                        child: Image.asset(
                          "images/facebook.png",
                          width: 30,
                          height: 30,
                        ),
                      ),
                      const Expanded(
                        child: Padding(
                          padding: EdgeInsets.only(right: 32.0),
                          child: Text(
                            "Sign In With Facebook",
                            style: TextStyle(color: praxisWhite),
                            textAlign: TextAlign.center,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              //Sign In with Google
              Container(
                decoration: BoxDecoration(
                    color: praxisWhite,
                    borderRadius: const BorderRadius.all(Radius.circular(5)),
                    boxShadow: [
                      BoxShadow(
                        color: Colors.grey.withOpacity(0.5),
                        spreadRadius: 5,
                        blurRadius: 7,
                      ),
                    ]),
                child: TextButton(
                  onPressed: () {},
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Padding(
                        padding: const EdgeInsets.only(left: 8.0),
                        child: Image.asset(
                          "images/google.png",
                          width: 30,
                          height: 30,
                        ),
                      ),
                      const Expanded(
                        child: Padding(
                          padding: EdgeInsets.only(right: 32.0),
                          child: Text(
                            "Sign In With Google",
                            style: TextStyle(color: praxisBlack),
                            textAlign: TextAlign.center,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              //Sign In with Apple
              Container(
                decoration: const BoxDecoration(
                  color: praxisBlack,
                  borderRadius: BorderRadius.all(Radius.circular(5)),
                ),
                child: TextButton(
                  onPressed: () {},
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Padding(
                        padding: const EdgeInsets.only(left: 8.0),
                        child: Image.asset(
                          "images/apple.png",
                          width: 25,
                          height: 25,
                        ),
                      ),
                      const Expanded(
                        child: Padding(
                          padding: EdgeInsets.only(right: 8.0),
                          child: Text(
                            "Sign In With Apple",
                            style: TextStyle(color: praxisWhite),
                            textAlign: TextAlign.center,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              //Divider (----or-----)
              Row(
                children: [
                  Expanded(
                    child: Container(
                      margin: const EdgeInsets.only(right: 10),
                      child: const Divider(color: praxisBlack),
                    ),
                  ),
                  const Text("or",
                      style: TextStyle(
                        color: praxisBlack,
                        fontWeight: FontWeight.bold,
                      )),
                  Expanded(
                    child: Container(
                      margin: const EdgeInsets.only(left: 10),
                      child: const Divider(color: praxisBlack),
                    ),
                  ),
                ],
              ),
              //Sign Up
              Container(
                decoration: const BoxDecoration(
                  color: praxisRed,
                  borderRadius: BorderRadius.all(Radius.circular(5)),
                ),
                child: TextButton(
                  onPressed: () async {
                    Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => CreateAccountView(),
                      ),
                    );
                  },
                  child: const Text(
                    "Sign Up",
                    style: TextStyle(color: praxisWhite),
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
