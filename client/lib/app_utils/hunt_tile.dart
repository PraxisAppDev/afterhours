import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/team_options.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class HuntTile extends StatelessWidget {
  final String title;
  final String date;
  final String location;
  
  const HuntTile({
    super.key,
    required this.title,
    required this.location,
    required this.date,
  });

  @override
  Widget build(BuildContext context) {
    return ListTile(
      title: Text(
        title,
        style: const TextStyle(
          fontWeight: FontWeight.bold,
          fontSize: 18,
        )
      ),
      subtitle: Column(
        children: [
          ListTile(
              leading: const Icon(Icons.location_on_sharp),
              title: Text(location),
          ),
          ListTile(
              leading: const Icon(Icons.calendar_month),
              title: Text(date),
          ),
        ],
      ),
      tileColor: praxisGrey,
      onTap: () => teamDialog(context, title),
    );
  }


  teamDialog(BuildContext context, String huntTitle) {
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return Container(
          alignment: Alignment.center,
          child: AlertDialog(
            insetPadding: const EdgeInsets.symmetric(vertical: 230),
            backgroundColor: praxisGrey,
            shape: RoundedRectangleBorder(
              borderRadius: BorderRadius.circular(20.0),
              side: const BorderSide(color: Colors.black),
            ),
            content: TeamOptions(huntTitle: huntTitle)
          ),
        );
      }
    );
  }
}