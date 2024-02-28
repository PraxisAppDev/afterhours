import 'package:flutter/material.dart';
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
            const Text('Hello world'),
          ]),
        ));
  }
}

// Build default from username for now
Widget buildProfileImage(
    String firstname, String lastname, double screenwidth) {
  // Extract initials from username
  String initials = firstname[0] + lastname[0];
  double avatarSize = screenwidth * 0.3;
  double fontSize = avatarSize * 0.5;

  return Padding(
    padding: const EdgeInsets.all(8.0),
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
