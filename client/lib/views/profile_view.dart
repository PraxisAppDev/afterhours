import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/profile_text_field.dart';
import 'package:praxis_afterhours/app_utils/profile_avatar.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/views/instructions.dart';

class ProfileView extends StatefulWidget {
  const ProfileView({super.key});

  @override
  State<ProfileView> createState() => _ProfileViewState();
}

class _ProfileViewState extends State<ProfileView> {
  final _formKey = GlobalKey<FormState>();

  @override
  Widget build(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    String firstName = 'Chell';
    String lastName = 'Lorem';

    return Scaffold(
      appBar: AppBar(
        centerTitle: false,
        title: const Text(
          'My Profile',
          style: TextStyle(
            color: praxisWhite,
            fontSize: 35,
          ),
        ),
        actions: [
          Padding(
              padding: const EdgeInsets.only(right: 8.0),
              child: IconButton(
                  onPressed: () => {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                              builder: (context) => const Instructions(
                                    title: 'Instructions',
                                  )),
                        )
                      },
                  icon: const Icon(Icons.info_outline))),
          Padding(
              padding: const EdgeInsets.only(right: 8.0),
              child: IconButton(
                  onPressed: () => {}, icon: const Icon(Icons.notifications))),
        ],
        backgroundColor: praxisRed,
      ),
      body: Column(children: [
        Form(
            key: _formKey,
            child:
                Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Center(
                child: Column(
                  children: [
                    ProfileAvatar(
                        firstName: firstName,
                        lastName: lastName,
                        screenWidth: screenWidth),
                    ProfileTextField(
                        defaultText: '$firstName $lastName',
                        label: 'Username',
                        icon: 'profile'),
                    ProfileTextField(
                      defaultText: '$firstName@gmail.com',
                      label: 'Email',
                      regex:
                          r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                      validatorMessage: 'Invalid email format',
                      icon: 'email',
                    ),
                    const ProfileTextField(
                      defaultText: '111-111-1111',
                      label: 'Phone Number',
                      regex:
                          r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$",
                      validatorMessage: 'Invalid phone number format',
                      icon: 'phone',
                    ),
                    Padding(
                        padding: const EdgeInsets.symmetric(vertical: 16),
                        child: ElevatedButton(
                          style: ButtonStyle(
                            backgroundColor:
                                MaterialStateProperty.all<Color>(praxisRed),
                            foregroundColor:
                                MaterialStateProperty.all<Color>(praxisWhite),
                            padding:
                                MaterialStateProperty.all<EdgeInsetsGeometry>(
                                    const EdgeInsets.all(18)),
                            shape: MaterialStateProperty.all<
                                RoundedRectangleBorder>(
                              RoundedRectangleBorder(
                                borderRadius:
                                    BorderRadius.circular(8), // BorderRadius
                              ),
                            ),
                            textStyle: MaterialStateProperty.all<TextStyle>(
                                const TextStyle(fontSize: 20)),
                          ),
                          onPressed: () {
                            if (_formKey.currentState!.validate()) {
                              ScaffoldMessenger.of(context).showSnackBar(
                                const SnackBar(content: Text('Changes Saved')),
                              );
                            }
                          },
                          child: const Text('Save Changes'),
                        ))
                  ],
                ),
              )
            ])),
      ]),
    );
  }
}
