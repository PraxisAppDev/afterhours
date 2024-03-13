import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/hunt_tile.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/entities/upcoming_hunt.dart';
import 'package:praxis_afterhours/service/upcoming_hunts_service.dart';
import 'package:praxis_afterhours/views/instructions.dart';

class JoinHuntView extends StatefulWidget {
  const JoinHuntView({super.key});

  @override
  State<JoinHuntView> createState() => _JoinHuntViewState();
}

class _JoinHuntViewState extends State<JoinHuntView> {
  late Future<List<UpcomingHunt>> futureHunts;

  @override
  void initState() {
    super.initState();
    futureHunts = fetchUpcomingHunts();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        centerTitle: false,
        title: const Text(
          "Join A Hunt",
          style: TextStyle(
            color: praxisWhite,
            fontSize: 35,
          ),
        ),
        automaticallyImplyLeading: false,
        actions: [
          Padding(
            padding: const EdgeInsets.only(right: 8.0),
            child: IconButton(
              onPressed: () => {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => const Instructions(
                      title: 'Instructions',
                    ),
                  ),
                ),
              },
              icon: const Icon(Icons.info_outline),
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(right: 8.0),
            child: IconButton(
              onPressed: () => {},
              icon: const Icon(Icons.notifications),
            ),
          )
        ],
        backgroundColor: praxisRed,
      ),
      body: FutureBuilder<List<UpcomingHunt>>(
        future: futureHunts,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            return Column(
              children: <Widget>[
                if (snapshot.data!.isEmpty)
                  const Center(
                    child: Padding(
                      padding: EdgeInsets.only(top: 32.0),
                      child: Text(
                        "No Hunts Available!",
                        style: TextStyle(fontSize: 35),
                      ),
                    ),
                  )
                else
                  for (UpcomingHunt upcomingHunt in snapshot.data ?? [])
                    Padding(
                      padding: const EdgeInsets.only(
                          top: 2, bottom: 2, left: 0, right: 0),
                      child: TextButton(
                        onPressed: () {},
                        child: HuntTile(
                          title: upcomingHunt.title,
                          location: upcomingHunt.location,
                          date: upcomingHunt.date,
                          onTapEnabled: true,
                        ),
                      ),
                    ),
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
