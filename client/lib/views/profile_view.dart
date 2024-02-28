import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/basic_text_field.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class ProfileView extends StatelessWidget {
  const ProfileView({super.key});

  @override
  Widget build(BuildContext context) {
    double screenwidth = MediaQuery.of(context).size.width;

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
                    onPressed: () => {}, icon: const Icon(Icons.info_outline))),
            Padding(
                padding: const EdgeInsets.only(right: 8.0),
                child: IconButton(
                    onPressed: () => {},
                    icon: const Icon(Icons.notifications))),
          ],
          backgroundColor: praxisRed,
        ),
        body: Center(
          child: Column(children: [
            buildProfileImage('Chell', 'Lorem', screenwidth),
            buildNameTextField(),
          ]),
        ));
  }
}

// Build default from username for now
Widget buildProfileImage(
    String firstName, String lastName, double screenWidth) {
  // Extract initials from username
  String initials = firstName[0] + lastName[0];
  double avatarSize = screenWidth * 0.3;
  double maxAvatarSize = 150;

  // Limit avatar size for larger screen
  if (screenWidth > 600) {
    avatarSize = maxAvatarSize;
  }

  double fontSize = avatarSize * 0.5;

  return Padding(
    padding: const EdgeInsets.all(20.0),
    child: Container(
        width: avatarSize,
        height: avatarSize,
        decoration: const BoxDecoration(
          shape: BoxShape.circle,
          color: praxisGrey,
        ),
        child: Center(
          child: Text(
            initials,
            style: TextStyle(
                color: Colors.white,
                fontWeight: FontWeight.bold,
                fontSize: fontSize),
          ),
        )),
  );
}

// Build from default username for now
Widget buildNameTextField() {
  return SizedBox(
    width: 200,
    height: 100,
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        const Padding(
          padding: EdgeInsets.symmetric(horizontal: 8, vertical: 16),
          child: TextField(
            maxLength: 20,
            decoration: InputDecoration(
              border: OutlineInputBorder(),
              hintText: 'Enter your username',
              counterText: '',
            ),
          ),
        ),
      ],
    ),
  );
}
