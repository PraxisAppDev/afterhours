import 'package:flutter/material.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class JoinTeamView extends StatelessWidget {
  const JoinTeamView({super.key});

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
      body: Column(
        children: [
          ExpansionTile(
            collapsedBackgroundColor: Color(0xFFE2E0E0),
            backgroundColor: Color(0xFFE2E0E0),
            tilePadding: EdgeInsets.all(12),
            title: Row(
              children: [
                Text(
                  "Aperture Science",
                  style: TextStyle(fontSize: 25),
                ),
                Spacer(),
                Icon(Icons.lock),
              ],
            ),
            collapsedShape: RoundedRectangleBorder(
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
                      "Members (4/4):",
                      style: TextStyle(fontSize: 20),
                    ),
                    SizedBox(height: 5),
                    Row(
                      children: [
                        Padding(
                          padding: EdgeInsets.only(left: 16.0),
                          child: Icon(Icons.circle),
                        ),
                        SizedBox(width: 5),
                        Text(
                          "Joe",
                          style: TextStyle(fontSize: 20),
                        ),
                        SizedBox(width: 200),
                        Icon(Icons.circle),
                        SizedBox(width: 5),
                        Text(
                          "Bob",
                          style: TextStyle(fontSize: 20),
                        ),
                      ],
                    ),
                    SizedBox(height: 10),
                    Row(
                      children: [
                        Padding(
                          padding: EdgeInsets.only(left: 16.0),
                          child: Icon(Icons.circle),
                        ),
                        SizedBox(width: 5),
                        Text(
                          "Jim",
                          style: TextStyle(fontSize: 20),
                        ),
                        SizedBox(width: 200),
                        Icon(Icons.circle),
                        SizedBox(width: 5),
                        Text(
                          "Frank",
                          style: TextStyle(fontSize: 20),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              ListTile(
                title: Text(
                  "This team is full!",
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 18),
                ),
              )
            ],
          ),
          ExpansionTile(
            tilePadding: EdgeInsets.all(12),
            title: Text(
              "The Billy Bobs",
              style: TextStyle(fontSize: 25),
            ),
            collapsedShape: RoundedRectangleBorder(
              side: BorderSide(
                color: praxisBlack,
                width: 1,
              ),
            ),
            controlAffinity: ListTileControlAffinity.leading,
            children: [
              const ListTile(
                title: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      "Members (3/4):",
                      style: TextStyle(fontSize: 20),
                    ),
                    SizedBox(height: 5),
                    Row(
                      children: [
                        Padding(
                          padding: EdgeInsets.only(left: 16.0),
                          child: Icon(Icons.circle),
                        ),
                        SizedBox(width: 5),
                        Text(
                          "Joe",
                          style: TextStyle(fontSize: 20),
                        ),
                        SizedBox(width: 200),
                        Icon(Icons.circle),
                        SizedBox(width: 5),
                        Text(
                          "Bob",
                          style: TextStyle(fontSize: 20),
                        ),
                      ],
                    ),
                    SizedBox(height: 10),
                    Row(
                      children: [
                        Padding(
                          padding: EdgeInsets.only(left: 16.0),
                          child: Icon(Icons.circle),
                        ),
                        SizedBox(width: 5),
                        Text(
                          "Dave",
                          style: TextStyle(fontSize: 20),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
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
          ),
          const ExpansionTile(
            collapsedBackgroundColor: Color(0xFFE2E0E0),
            backgroundColor: Color(0xFFE2E0E0),
            tilePadding: EdgeInsets.all(12),
            title: Row(
              children: [
                Text(
                  "The Charlie Cats",
                  style: TextStyle(
                    fontSize: 25,
                  ),
                ),
                Spacer(),
                Icon(Icons.lock),
              ],
            ),
            collapsedShape: RoundedRectangleBorder(
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
                      "Members (2/4):",
                      style: TextStyle(fontSize: 20),
                    ),
                    SizedBox(height: 5),
                    Row(
                      children: [
                        Padding(
                          padding: EdgeInsets.only(left: 16.0),
                          child: Icon(Icons.circle),
                        ),
                        SizedBox(width: 5),
                        Text(
                          "Joe",
                          style: TextStyle(fontSize: 20),
                        ),
                        SizedBox(width: 200),
                        Icon(Icons.circle),
                        SizedBox(width: 5),
                        Text(
                          "Bob",
                          style: TextStyle(fontSize: 20),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
              ListTile(
                title: Text(
                  "This team is locked!",
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 18),
                ),
              )
            ],
          ),
          // Expanded(
          //   child: Align(
          //     alignment: Alignment.bottomCenter,
          //     child: Padding(
          //       padding: const EdgeInsets.all(8.0),
          //       child: Container(
          //         color: const Color(0xFFEEEEEE),
          //         child: TextButton(
          //           onPressed: () {},
          //           child: const SizedBox(
          //             width: double.infinity,
          //             child: Text(
          //               "Join Team",
          //               style: TextStyle(fontSize: 25),
          //               textAlign: TextAlign.center,
          //             ),
          //           ),
          //         ),
          //       ),
          //     ),
          //   ),
          // )
        ],
      ),
    );
  }
}
