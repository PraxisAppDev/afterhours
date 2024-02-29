import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/team_options.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class ProfileTextField extends StatefulWidget {
  final String label;
  final String icon;
  final String defaultText;

  const ProfileTextField(
      {super.key, required this.defaultText, this.label = '', this.icon = ''});

  @override
  State<ProfileTextField> createState() => _ProfileTextFieldState();
}

class _ProfileTextFieldState extends State<ProfileTextField> {
  bool isEditing = false;
  late TextEditingController controller;

  @override
  void initState() {
    super.initState();
    controller = TextEditingController(text: widget.defaultText);
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        ListTile(
            leading: getIcon(widget.icon),
            subtitle: TextFormField(
              controller: controller,
              decoration: InputDecoration(
                labelText: widget.label,
                labelStyle: const TextStyle(
                    fontSize: 18), // Adjust the font size as needed
                // Add other InputDecoration properties as needed
              ),
              enabled: isEditing,
              onFieldSubmitted: (value) {
                setState(() {
                  controller.text = value;
                  isEditing = false;
                });
              },
            ),
            trailing: isEditing
                ? null
                : IconButton(
                    icon: Icon(Icons.edit),
                    onPressed: () {
                      setState(() {
                        isEditing = true;
                      });
                    })),
        const Divider(color: praxisBlack)
      ],
    );
  }

  @override
  void dispose() {
    controller.dispose(); // Dispose of the controller when no longer needed
    super.dispose();
  }
}

Icon getIcon(String icon) {
  switch (icon) {
    case 'email':
      return const Icon(Icons.email);
    case 'phone':
      return const Icon(Icons.phone);
    case 'profile':
      return const Icon(Icons.person, size: 30);
    default:
      return const Icon(null);
  }
}
