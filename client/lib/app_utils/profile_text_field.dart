import 'package:flutter/material.dart';

class ProfileTextField extends StatelessWidget {
  final TextEditingController editingController;
  final String label;
  final String defaultText;
  final String regex;
  final String validatorMessage;
  final String icon;

  const ProfileTextField({
    super.key,
    required this.editingController,
    required this.label,
    required this.defaultText,
    this.regex = '.',
    this.validatorMessage = 'Invalid format',
    this.icon = '',
  });

  @override
  Widget build(BuildContext context) {
    bool showSuffixIcon = true;

    editingController.text = defaultText;

    return Padding(
      padding: const EdgeInsets.only(left: 30, top: 8, right: 30, bottom: 8),
      child: TextFormField(
        controller: editingController,
        decoration: InputDecoration(
          prefixIcon: getIcon(icon),
          suffixIcon: showSuffixIcon ? const Icon(Icons.edit) : null,
          labelText: label,
          border: const OutlineInputBorder(),
        ),
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'This field cannot be empty';
          }
          RegExp regExp = RegExp(regex);
          if (!regExp.hasMatch(value)) {
            return validatorMessage;
          }
          return null; // input is valid
        },
        textInputAction: TextInputAction.none,
      ),
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
