import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/basic_text_field.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class ProfileView extends StatelessWidget {
  const ProfileView({super.key});

  @override
  Widget build(BuildContext context) {
    double screenwidth = MediaQuery.of(context).size.width;
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
            buildProfileImage(firstName, lastName, screenwidth),
            Container(
                decoration: BoxDecoration(
                    border: Border.all(color: praxisBlack),
                    borderRadius: BorderRadius.circular(10)),
                child: Padding(
                  padding: const EdgeInsets.all(40.0),
                  child: Column(children: [
                    buildTextField(firstName + ' ' + lastName, 'Username'),
                    buildTextField(firstName + '@gmail.com', 'Email'),
                    buildTextField('111-111-111', 'Phone-Number'),
                  ]),
                ))
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
Widget buildTextField(String defaultText, String hintText) {
  TextEditingController usernameController =
      TextEditingController(text: defaultText);

  return SizedBox(
    width: 200,
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 16),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(hintText),
                TextField(
                    controller: usernameController,
                    maxLength: 30,
                    decoration: InputDecoration(
                      border: const OutlineInputBorder(),
                      hintText: hintText,
                      counterText: '',
                    )),
              ],
            )),
      ],
    ),
  );
}
