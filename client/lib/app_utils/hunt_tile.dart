import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/team_options.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class HuntTile extends StatelessWidget {
  final String title;
  final String date;
  final String location;
  final bool onTapEnabled;
  final String trailing;

  const HuntTile({
    super.key,
    required this.title,
    required this.location,
    required this.date,
    required this.onTapEnabled,
    this.trailing = '',
  });

  @override
  Widget build(BuildContext context) {
    return ListTile(
        title: Text(title,
            style: const TextStyle(
              fontWeight: FontWeight.bold,
              fontSize: 18,
            )),
        subtitle: Column(
          children: [
            ListTile(
                leading: const Icon(Icons.location_on_sharp),
                title: Text(location),
                trailing: trailing == '' ? null : getPlaceText(trailing)),
            ListTile(
              leading: const Icon(Icons.calendar_month),
              title: Text(date),
            ),
          ],
        ),
        tileColor: praxisGrey,
        onTap: onTapEnabled ? () => teamDialog(context, title) : null);
  }

  teamDialog(BuildContext context, String huntTitle) {
    showDialog(
        context: context,
        builder: (BuildContext context) {
          return Container(
            alignment: Alignment.center,
            child: AlertDialog(
                insetPadding: const EdgeInsets.symmetric(vertical: 215),
                backgroundColor: praxisGrey,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(20.0),
                  side: const BorderSide(color: Colors.black),
                ),
                content: TeamOptions(huntTitle: huntTitle)),
          );
        });
  }
}

String getPlaceStr(String place) {
  switch (place) {
    case '1':
      return '${place}st';
    case '2':
      return '${place}nd';
    case '3':
      return '${place}rd';
    default:
      return '${place}th';
  }
}

Widget getPlaceText(String place) {
  return Column(
    children: [
      Text(getPlaceStr(place),
          style: const TextStyle(
            fontWeight: FontWeight.bold,
            fontSize: 20,
          )),
      const Text('place',
          style: TextStyle(
            fontSize: 12,
          ))
    ],
  );
}
