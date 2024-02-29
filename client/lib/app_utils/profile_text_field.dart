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
  @override
  Widget build(BuildContext context) {
    TextEditingController controller =
        TextEditingController(text: widget.defaultText);

    return ListTile(
      leading: getIcon(widget.icon),
      subtitle: TextFormField(
          controller: controller,
          decoration: InputDecoration(
            labelText: widget.label,
            labelStyle:
                const TextStyle(fontSize: 18), // Adjust the font size as needed
            // Add other InputDecoration properties as needed
          )),
      //trailing: IconButton(onPressed: () {}, icon: const Icon(Icons.edit))
    );
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
