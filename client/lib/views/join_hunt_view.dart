import 'package:flutter/material.dart';
import 'package:praxis_afterhours/app_utils/hunt_tile.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class JoinHuntView extends StatelessWidget {
  const JoinHuntView({super.key});

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
        actions: [
          Padding(
            padding: const EdgeInsets.only(right: 8.0),
            child: IconButton(
              onPressed: () => {},
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
      body: Column(
        children: <Widget>[
          Padding(
            padding:
                const EdgeInsets.only(top: 2, bottom: 2, left: 0, right: 0),
            child: TextButton(
              onPressed: () {},
              child: const HuntTile(
                title: "Recruit Mixer",
                location: "The Greene Turtle (In-Person Only)",
                date: "01/30/024 at 8:30 PM",
              ),
            ),
          ),
          Padding(
            padding:
                const EdgeInsets.only(top: 2, bottom: 2, left: 0, right: 0),
            child: TextButton(
              onPressed: () async {},
              child: const HuntTile(
                title: "Friday Employee Drinks",
                location: "Looney's Pub",
                date: "02/07/2024 at 7:30 PM",
              ),
            ),
          ),
          Padding(
            padding:
                const EdgeInsets.only(top: 2, bottom: 2, left: 0, right: 0),
            child: TextButton(
              onPressed: () async {},
              child: const HuntTile(
                title: "End of Quarter Party",
                location: "Cornerstone Grill & Loft",
                date: "02/14/2024 at 7:00 PM",
              ),
            ),
          ),
        ],
      ),
    );
  }
}
