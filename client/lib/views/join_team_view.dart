import 'package:flutter/material.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/entities/team.dart';
import 'package:praxis_afterhours/service/teams_service.dart';

class JoinTeamView extends StatefulWidget {
  const JoinTeamView({super.key});

  @override
  State<JoinTeamView> createState() => _JoinTeamViewState();
}

class _JoinTeamViewState extends State<JoinTeamView> {
  late Future<List<Team>> futureTeams;

  @override
  void initState() {
    super.initState();
    futureTeams = fetchTeams();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.arrow_back),
          onPressed: () async {
            Navigator.pop(context);
          },
        ),
        title: const Text(
          "Join Team",
          style: TextStyle(
            color: praxisWhite,
            fontSize: 35,
          ),
        ),
        bottom: PreferredSize(
          preferredSize: const Size.fromHeight(kToolbarHeight),
          child: Container(
            color: praxisWhite,
            child: const TextField(
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                hintText: "Search for a team name",
              ),
            ),
          ),
        ),
        backgroundColor: praxisRed,
      ),
      body: FutureBuilder<List<Team>>(
        future: futureTeams,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return Column(
              children: <Widget>[
                for (Team team in snapshot.data ?? [])
                  ExpansionTile(
                    collapsedBackgroundColor: team.isFull
                        ? const Color(0xFFE2E0E0)
                        : const Color(0xFFFFFFFF),
                    backgroundColor: team.isFull
                        ? const Color(0xFFE2E0E0)
                        : const Color(0xFFFFFFFF),
                    tilePadding: const EdgeInsets.all(12),
                    title: Row(
                      children: [
                        Text(
                          team.teamName,
                          style: const TextStyle(fontSize: 25),
                        ),
                        const Spacer(),
                        if (team.isFull) const Icon(Icons.lock),
                      ],
                    ),
                    collapsedShape: const RoundedRectangleBorder(
                      side: BorderSide(
                        color: praxisBlack,
                        width: 1,
                      ),
                    ),
                    controlAffinity: ListTileControlAffinity.leading,
                    children: [
                      ListTile(
                        title: Column(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Text(
                              "Members (${team.teamMembers.length}/${team.capacity}):",
                              style: const TextStyle(fontSize: 20),
                            ),
                            for (var i = 0;
                                i < team.teamMembers.length ~/ 2 * 2;
                                i += 2)
                              Column(
                                children: [
                                  if (i == 0)
                                    const SizedBox(height: 5)
                                  else
                                    const SizedBox(height: 10),
                                  Row(
                                    children: [
                                      const Padding(
                                        padding: EdgeInsets.only(left: 16.0),
                                        child: Icon(Icons.circle),
                                      ),
                                      const SizedBox(width: 5),
                                      Text(
                                        team.teamMembers[i],
                                        style: const TextStyle(fontSize: 20),
                                      ),
                                      const SizedBox(width: 200),
                                      const Icon(Icons.circle),
                                      const SizedBox(width: 5),
                                      Text(
                                        team.teamMembers[i + 1],
                                        style: const TextStyle(fontSize: 20),
                                      ),
                                    ],
                                  ),
                                ],
                              ),
                            for (var i = team.teamMembers.length ~/ 2 * 2;
                                i < team.teamMembers.length;
                                i += 2)
                              Column(
                                children: [
                                  if (team.teamMembers.length == 1)
                                    const SizedBox(height: 5)
                                  else
                                    const SizedBox(height: 10),
                                  Row(
                                    children: [
                                      const Padding(
                                        padding: EdgeInsets.only(left: 16.0),
                                        child: Icon(Icons.circle),
                                      ),
                                      const SizedBox(width: 5),
                                      Text(
                                        team.teamMembers[i],
                                        style: const TextStyle(fontSize: 20),
                                      ),
                                    ],
                                  ),
                                ],
                              )
                          ],
                        ),
                      ),
                      if (team.isFull)
                        ListTile(
                          title: Text(
                            switch (team.reasonFull) {
                              "capacity_reached" => "This team is full!",
                              "team_locked" => "This team is locked!",
                              _ => throw const FormatException(
                                  "Invalid reason_full")
                            },
                            textAlign: TextAlign.center,
                            style: const TextStyle(fontSize: 18),
                          ),
                        )
                      else
                        ListTile(
                          title: Container(
                            decoration: const BoxDecoration(
                              borderRadius: BorderRadius.all(
                                Radius.circular(5),
                              ),
                              color: praxisRed,
                            ),
                            child: TextButton(
                              onPressed: () {},
                              child: const Text(
                                "Join Team",
                                style: TextStyle(
                                  fontSize: 18,
                                  color: praxisWhite,
                                ),
                              ),
                            ),
                          ),
                        ),
                    ],
                  )
              ],
            );
          } else if (snapshot.hasError) {
            return Text("${snapshot.error}");
          }

          return const CircularProgressIndicator();
        },
      ),
    );
  }
}
