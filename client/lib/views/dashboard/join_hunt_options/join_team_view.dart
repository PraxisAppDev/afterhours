import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter_animate/flutter_animate.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:page_transition/page_transition.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/reusables/hunt_structure.dart';
import 'package:praxis_afterhours/views/dashboard/join_hunt_options/waiting_room_view.dart';
import 'package:http/http.dart' as http;

class JoinTeamView extends StatefulWidget {
  final String huntId;
  const JoinTeamView({
    super.key,
    required this.huntId,
  });

  @override
  State<JoinTeamView> createState() => _JoinTeamViewState();
}

class _JoinTeamViewState extends State<JoinTeamView> {
  List<Team> _teams = [];
  final TextEditingController _searchController = TextEditingController();
  String _searchQuery = '';
  late final String huntId;

  @override
  void initState() {
    super.initState();
    huntId = widget.huntId;
    _fetchTeams();
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _fetchTeams() async {
    final response =
        await http.get(Uri.parse('http://localhost:8001/teams/get_teams?id_hunt=$huntId'));

    if (response.statusCode == 200) {
      final jsonData = json.decode(response.body);
      final List<dynamic> teamData = jsonData['content'];
      
      setState(() {
        _teams = teamData.map((team) => Team.fromJson(team)).toList();
      });
    } else {
      // Handle error case
      if(kDebugMode) print('Failed to fetch upcoming hunts');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: CustomScrollView(
        slivers: [
          SliverAppBar(
            expandedHeight: 240,
            pinned: true,
            floating: true,
            leading: IconButton(
              icon: const Icon(Icons.arrow_back),
              onPressed: () async {
                Navigator.pop(context);
              },
            ),
            flexibleSpace: FlexibleSpaceBar(
              titlePadding: const EdgeInsets.only(
                left: 16,
                bottom: 100,
              ),
              centerTitle: false,
              title: Align(
                alignment: Alignment.bottomLeft,
                child: Text(
                  "Select a Team",
                  style: GoogleFonts.poppins(
                    color: Colors.white,
                    fontSize: 32,
                  ),
                  textAlign: TextAlign.start,
                ),
              ),
            ),
            bottom: PreferredSize(
              preferredSize: const Size.fromHeight(kToolbarHeight),
              child: Padding(
                padding: const EdgeInsets.only(left: 16, right: 16),
                child: Column(
                  children: [
                    Container(
                      color: praxisRed,
                      child: BasicTextField(
                        editingController: _searchController,
                        labelText: "Search for a team",
                        labelStyle: GoogleFonts.poppins(
                          color: praxisWhite,
                          fontSize: 16,
                        ),
                        fieldType: BasicTextFieldType.custom,
                        validatorError: "Please enter a team name",
                        keyboardType: TextInputType.text,
                        onChange: (value) {
                          setState(() {
                            _searchQuery = value;
                          });
                        },
                      ),
                    ),
                    const SizedBox(
                      height: 15,
                    ),
                  ],
                ),
              ),
            ),
            backgroundColor: praxisRed,
            elevation: 0,
          ),
          SliverPadding(
            padding: const EdgeInsets.all(16),
            sliver: SliverList(
              delegate: SliverChildListDelegate(
                _buildFilteredTeamTiles(),
              ),
            ),
          ),
        ],
      ),
    );
  }

  List<Widget> _buildFilteredTeamTiles() {

    List<Widget> teamTiles = [];
    for (Team team in _teams) {
      teamTiles.add(
        _buildTeamTile(team.name, team.players.length, team.capacity, team.players, team.isLocked, context)
      );
    }

    final filteredTiles = teamTiles.where((tile) {
      final teamName = tile.key.toString().toLowerCase();
      final searchQuery = _searchQuery.toLowerCase();
      return teamName.contains(searchQuery);
    }).toList();

    return filteredTiles.map((tile) {
      final index = filteredTiles.indexOf(tile);
      return tile
          .animate(delay: 150.milliseconds * index + 150.milliseconds)
          .fade()
          .slideY(
            begin: 0.5,
            end: 0,
          );
    }).toList();
  }

  Widget _buildTeamTile(
    String teamName,
    int currentMembers,
    int capacity,
    List<String> memberNames,
    bool isLocked,
    BuildContext context,
  ) {
    return Card(
      key: Key(teamName),
      elevation: 4,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(16),
      ),
      child: Theme(
        data: Theme.of(context).copyWith(
          dividerColor: Colors.transparent,
        ),
        child: ExpansionTile(
          initiallyExpanded: true,
          title: Row(
            children: [
              Text(
                teamName,
                style: const TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const Spacer(),
              if (isLocked) const Icon(Icons.lock, color: Colors.grey),
            ],
          ),
          children: [
            Padding(
              padding: const EdgeInsets.symmetric(horizontal: 16),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "Members ($currentMembers/$capacity):",
                    style: const TextStyle(fontSize: 16),
                    textAlign: TextAlign.start,
                  ),
                  const SizedBox(height: 8),
                  Wrap(
                    alignment: WrapAlignment.start,
                    spacing: 16,
                    children: memberNames.map((name) {
                      return Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          const Icon(Icons.person, color: Colors.grey),
                          const SizedBox(width: 4),
                          Text(name, style: const TextStyle(fontSize: 16)),
                        ],
                      );
                    }).toList(),
                  ),
                  const SizedBox(height: 16),
                  if (currentMembers == capacity)
                    Container(
                      width: double.infinity,
                      child: const Text(
                        "This team is full!",
                        textAlign: TextAlign.center,
                        style: TextStyle(fontSize: 16, color: Colors.red),
                      ),
                    )
                  else if (isLocked)
                    Container(
                      width: double.infinity,
                      child: const Text(
                        "This team is locked!",
                        textAlign: TextAlign.center,
                        style: TextStyle(fontSize: 16, color: Colors.red),
                      ),
                    )
                  else
                    SizedBox(
                      width: double.infinity,
                      child: GestureDetector(
                        onTap: () {
                          Navigator.push(
                              context,
                              PageTransition(
                                type: PageTransitionType.rightToLeft,
                                child: const WaitingRoomView(),
                              ));
                        },
                        child: Container(
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(16),
                            color: praxisRed,
                          ),
                          child: const Padding(
                            padding: EdgeInsets.symmetric(vertical: 16),
                            child: Text(
                              'Join Team',
                              style: TextStyle(
                                fontSize: 16,
                                color: Colors.white,
                                fontWeight: FontWeight.bold,
                              ),
                              textAlign: TextAlign.center,
                            ),
                          ),
                        ),
                      ),
                    ),
                  const SizedBox(height: 16),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}

enum BasicTextFieldType {
  email,
  password,
  username,
  custom,
}

class BasicTextField extends StatelessWidget {
  final TextEditingController editingController;
  final String labelText;
  final BasicTextFieldType fieldType;
  final String validatorError;
  final TextInputType keyboardType;
  final bool obscureText;
  final Function(String)? onChange;
  final TextStyle labelStyle;

  const BasicTextField({
    super.key,
    required this.editingController,
    required this.labelText,
    this.fieldType = BasicTextFieldType.custom,
    required this.validatorError,
    this.keyboardType = TextInputType.text,
    this.obscureText = false,
    this.onChange,
    this.labelStyle = const TextStyle(fontSize: 16),
  });

  String? validatorFunction(String? value) {
    if (value == null || value.isEmpty) {
      return validatorError;
    }
    switch (fieldType) {
      case BasicTextFieldType.email:
        final emailRegex =
            RegExp(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$");
        if (!emailRegex.hasMatch(value)) {
          return 'Invalid email format';
        }
        break;
      case BasicTextFieldType.password:
        if (value.length < 8) {
          return 'Password should be at least 6 characters long';
        }
        final passwordRegex = RegExp(
            r"^(?=.{8,})(?=.*[a-zA-Z])(?=.*[0-9])(?=.*[!@#$%^&*(),.+=]).*$");
        if (!passwordRegex.hasMatch(value)) {
          return 'Invalid password';
        }
        break;
      case BasicTextFieldType.username:
        if (value.length < 3) {
          return 'Username should be at least 3 characters long';
        }
        break;
      case BasicTextFieldType.custom:
        break;
    }
    return null;
  }

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      keyboardType: keyboardType,
      obscureText: obscureText,
      validator: validatorFunction,
      controller: editingController,
      onChanged: onChange,
      style: const TextStyle(color: Colors.white),
      decoration: InputDecoration(
        labelText: labelText,
        labelStyle: labelStyle,
        focusedBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: Colors.white),
        ),
        enabledBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: Colors.white),
        ),
        errorBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: Colors.red),
        ),
        focusedErrorBorder: const UnderlineInputBorder(
          borderSide: BorderSide(color: Colors.red),
        ),
        border: const UnderlineInputBorder(),
      ),
    );
  }
}
