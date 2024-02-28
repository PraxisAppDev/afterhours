import 'package:flutter/material.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/views/create_team_view.dart';
import 'package:praxis_afterhours/views/hunt_alone.dart';
import 'package:praxis_afterhours/views/join_team_view.dart';

class TeamOptions extends StatelessWidget {
  final String huntTitle;
  const TeamOptions({
    super.key,
    required this.huntTitle,
  });

  final padding = const EdgeInsets.only(
    bottom: 8.0,
    top: 8.0,
    left: 2.0,
    right: 2.0
  );


  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Center(child: Text("How do you want to join $huntTitle?", style: const TextStyle(fontSize: 28, fontWeight: FontWeight.bold))),
          ),
          Padding(
            padding: padding,
            child: TextButton(
              onPressed: () {
                Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => const JoinTeamView(),
                      ),
                    );
              },
              child: const ListTile(
                title: Center(child: Text("Join Team", style: TextStyle(fontSize: 28))),
                tileColor: praxisGrey,
              )
            ),
          ),
          Padding(
            padding: padding,
            child: TextButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => CreateTeamView(),
                  ),
                );
              },
              child: const ListTile(
                title: Center(child: Text("Create Team", style: TextStyle(fontSize: 28))),
                tileColor: praxisGrey,
              )
            ),
          ),
          Padding(
            padding: padding,
            child: TextButton(
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => HuntAloneView(),
                  )
                );
              },
              child: const ListTile(
                title: Center(child: Text("Hunt Alone", style: TextStyle(fontSize: 28))),
                tileColor: praxisGrey,
              )
            ),
          ),
        ],
      )
    );
  }
}