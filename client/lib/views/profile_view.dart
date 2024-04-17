import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/profile_text_field.dart';
import 'package:praxis_afterhours/app_utils/profile_avatar.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/views/instructions.dart';
import 'package:praxis_afterhours/apis/profile_api.dart';
import 'package:praxis_afterhours/apis/auth_api.dart';
import 'package:praxis_afterhours/views/sign_in_view.dart';

class ProfileView extends StatefulWidget {
  const ProfileView({super.key});

  @override
  State<ProfileView> createState() => _ProfileViewState();
}

class _ProfileViewState extends State<ProfileView> {
  final _formKey = GlobalKey<FormState>();

  TextEditingController usernameController = TextEditingController();
  TextEditingController emailController = TextEditingController();
  TextEditingController phoneNumberController = TextEditingController();
  TextEditingController fullnameController = TextEditingController();

  @override
  void dispose() {
    usernameController.dispose();
    emailController.dispose();
    phoneNumberController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;

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
        automaticallyImplyLeading: false,
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
      body: FutureBuilder(
          future: fetchUserInfo(),
          builder: (context, snapshot) {
            if (snapshot.connectionState == ConnectionState.waiting) {
              return const CircularProgressIndicator();
            }
            if (snapshot.hasError) {
              return Text(snapshot.error.toString());
            } else {
              String fullname = '';
              String username = '';
              String firstName = '';
              String lastName = '';
              String email = '';
              String phoneNumber = '';

              // Parse json data
              var userInfo = snapshot.data;
              if (userInfo != null) {
                var content = userInfo['content'];
                username = content['username'];
                fullname = content['fullname'];
                List<String> fullnameSplit = content['fullname'].split(' ');
                firstName = fullnameSplit[0];

                // If last name exists
                if (fullnameSplit.length > 1) {
                  lastName = fullnameSplit[1];
                }
                email = content['email'];
                phoneNumber = content['phone'] ?? '';
              }

              return Column(children: [
                Form(
                    key: _formKey,
                    child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Center(
                            child: Column(
                              children: [
                                ProfileAvatar(
                                    firstName: firstName,
                                    lastName: lastName,
                                    screenWidth: screenWidth),
                                ProfileTextField(
                                    editingController: fullnameController,
                                    defaultText: fullname,
                                    label: 'Full name',
                                    icon: 'profile'),
                                ProfileTextField(
                                    editingController: usernameController,
                                    defaultText: username,
                                    label: 'Username',
                                    icon: 'profile'),
                                ProfileTextField(
                                  editingController: emailController,
                                  defaultText: email,
                                  label: 'Email',
                                  regex:
                                      r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",
                                  validatorMessage: 'Invalid email format',
                                  icon: 'email',
                                ),
                                ProfileTextField(
                                  editingController: phoneNumberController,
                                  defaultText: phoneNumber,
                                  label: 'Phone Number',
                                  regex:
                                      r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$",
                                  validatorMessage:
                                      'Invalid phone number format',
                                  icon: 'phone',
                                ),
                                Padding(
                                    padding: const EdgeInsets.symmetric(
                                        vertical: 16),
                                    child: ElevatedButton(
                                      style: ButtonStyle(
                                        backgroundColor:
                                            MaterialStateProperty.all<Color>(
                                                praxisRed),
                                        foregroundColor:
                                            MaterialStateProperty.all<Color>(
                                                praxisWhite),
                                        padding: MaterialStateProperty.all<
                                                EdgeInsetsGeometry>(
                                            const EdgeInsets.all(18)),
                                        shape: MaterialStateProperty.all<
                                            RoundedRectangleBorder>(
                                          RoundedRectangleBorder(
                                            borderRadius: BorderRadius.circular(
                                                8), // BorderRadius
                                          ),
                                        ),
                                        textStyle: MaterialStateProperty.all<
                                                TextStyle>(
                                            const TextStyle(fontSize: 20)),
                                      ),
                                      onPressed: () {
                                        if (_formKey.currentState!.validate()) {
                                          _submitForm(userInfo);
                                          ScaffoldMessenger.of(context)
                                              .showSnackBar(
                                            const SnackBar(
                                                content: Text('Changes Saved')),
                                          );
                                        }
                                      },
                                      child: const Text('Save Changes'),
                                    )),
                                Padding(
                                    padding: const EdgeInsets.symmetric(
                                        vertical: 16),
                                    child: ElevatedButton(
                                      style: ButtonStyle(
                                        backgroundColor:
                                            MaterialStateProperty.all<Color>(
                                                praxisRed),
                                        foregroundColor:
                                            MaterialStateProperty.all<Color>(
                                                praxisWhite),
                                        padding: MaterialStateProperty.all<
                                                EdgeInsetsGeometry>(
                                            const EdgeInsets.all(18)),
                                        shape: MaterialStateProperty.all<
                                            RoundedRectangleBorder>(
                                          RoundedRectangleBorder(
                                            borderRadius: BorderRadius.circular(
                                                8), // BorderRadius
                                          ),
                                        ),
                                        textStyle: MaterialStateProperty.all<
                                                TextStyle>(
                                            const TextStyle(fontSize: 20)),
                                      ),
                                      onPressed: () {
                                        logoutUser();
                                        Navigator.pushReplacement(
                                          context,
                                          MaterialPageRoute(
                                            builder: (context) => SignInView(),
                                          ),
                                        );
                                      },
                                      child: const Text('Logout'),
                                    ))
                              ],
                            ),
                          )
                        ])),
              ]);
            }
          }),
    );
  }

  void _submitForm(Map<String, dynamic>? userInfo) async {
    if (userInfo != null) {
      String fullname = fullnameController.text;
      String username = usernameController.text;
      String email = emailController.text;
      String phoneNumber = phoneNumberController.text;

      final updatedUserInfo = {
        ...userInfo['content'],
        "fullname": fullname,
        "username": username,
        "email": email,
        "phone": phoneNumber.isNotEmpty ? phoneNumber : null,
      };

      await updateUserInfo(updatedUserInfo);
    }
  }
}
