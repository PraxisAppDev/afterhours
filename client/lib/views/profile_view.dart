import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/profile_text_field.dart';
import 'package:praxis_afterhours/app_utils/profile_avatar.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/views/instructions.dart';

class ProfileView extends StatelessWidget {
  const ProfileView({super.key});

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
                    onPressed: () => {},
                    icon: const Icon(Icons.notifications))),
          ],
          backgroundColor: praxisRed,
        ),
        body: Column(
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
                      defaultText: '${firstName} ${lastName}',
                      label: 'Username',
                      icon: 'profile'),
                ],
              ),
            ),
            ProfileTextField(
                defaultText: '${firstName}@gmail.com',
                label: 'Email',
                icon: 'email'),
            ProfileTextField(
                defaultText: '111-111-111',
                label: 'Phone Number',
                icon: 'phone')
          ],
        ));
  }
}
