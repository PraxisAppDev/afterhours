import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:praxis_afterhours/views/team/edit_team_view.dart';

import '../../reusables/hunt_structure.dart';

import '../../apis/teams_api.dart' as teamsApi;

class CreateTeamView extends StatelessWidget {
  final Hunt hunt;
  final String initialTeamName;

  const CreateTeamView({super.key, required this.hunt, required this.initialTeamName});

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
      future: teamsApi.createTeam(hunt.id, initialTeamName),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          if(snapshot.hasError) {
            return Center(
              child: Text(
                snapshot.error.toString(),
                style: const TextStyle(
                  color: Colors.red,
                  fontSize: 24,
                ),
              ),
            );
          } else {
            return TeamMembersView(
              team: snapshot.data!,
              hunt: hunt,
              editMode: true,
            );
          }
        } else {
          return const Center(
            child: CircularProgressIndicator(),
          );
        }
      },
    );
  }
}