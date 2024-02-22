import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/basic_text_field.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class CreateAccountView extends StatelessWidget {
  CreateAccountView({super.key});
  final margins = const EdgeInsets.only(
    top: 32,
    bottom: 32,
    left: 32,
    right: 32,
  );

  final _formKey = GlobalKey<FormState>();

  String error = "";

  TextEditingController usernameController = TextEditingController();
  TextEditingController fullNameController = TextEditingController();
  TextEditingController emailController = TextEditingController();
  TextEditingController passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        margin: margins,
        child: Form(
          key: _formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Container(
                  alignment: Alignment.topLeft,
                  child: IconButton(
                    icon: const Icon(Icons.arrow_back),
                    onPressed: () async {
                      Navigator.pop(context);
                    },
                  )),
              Container(
                alignment: Alignment.bottomCenter,
                child: const FittedBox(
                  fit: BoxFit.scaleDown,
                  child:
                      Text("Create an Account", style: TextStyle(fontSize: 36)),
                ),
              ),
              Container(
                padding: const EdgeInsets.all(8.0),
                margin: const EdgeInsets.all(12.0),
                child: BasicTextField(
                  labelText: "Username",
                  fieldType: BasicTextFieldType.username,
                  editingController: usernameController,
                  validatorError: "Please enter a username",
                ),
              ),
              Container(
                alignment: Alignment.center,
                margin: const EdgeInsets.all(12.0),
                child: BasicTextField(
                  labelText: "Full Name",
                  fieldType: BasicTextFieldType.custom,
                  editingController: fullNameController,
                  validatorError: "Please enter your name",
                ),
              ),
              Container(
                alignment: Alignment.center,
                margin: const EdgeInsets.all(12.0),
                child: BasicTextField(
                  labelText: "Email Address",
                  fieldType: BasicTextFieldType.email,
                  editingController: emailController,
                  validatorError: "Please enter your email",
                ),
              ),
              Container(
                alignment: Alignment.center,
                margin: const EdgeInsets.all(12.0),
                child: BasicTextField(
                  labelText: "Password",
                  fieldType: BasicTextFieldType.password,
                  editingController: passwordController,
                  validatorError: "Please enter a password",
                  obscureText: true,
                ),
              ),
              Container(
                alignment: Alignment.centerLeft,
                margin: const EdgeInsets.all(12.0),
                child: const Text(
                    "Your password must have\n • At least 8 characters\n • At least one number\n • At least one special character"),
              ),
              Container(
                margin: const EdgeInsets.all(12.0),
                decoration: const BoxDecoration(
                  color: praxisRed,
                  borderRadius: BorderRadius.all(Radius.circular(5)),
                ),
                child: TextButton(
                  onPressed: () async {
                    if (_formKey.currentState!.validate()) {
                      //insert create account logic here
                    }
                  },
                  child: const Text("Sign Up",
                      style: TextStyle(
                        color: praxisWhite,
                      )),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
