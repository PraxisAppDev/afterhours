import 'package:flutter/material.dart';
import 'package:fluttertoast/fluttertoast.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/apis/teams_api.dart' as teamsApi;

import '../../reusables/hunt_structure.dart';

class TeamMembersView extends StatefulWidget {
  final Team team;
  final Hunt hunt;
  final bool editMode;

  const TeamMembersView({super.key, required this.team, required this.hunt, required this.editMode});

  @override
  State<TeamMembersView> createState() => _TeamMembersViewState();
}

class _TeamMembersViewState extends State<TeamMembersView> {
  final List<String> _teamMembers = ['Chell', 'GLaDOS', 'Wheatley'];
  final int _maxTeamSize = 4;

  void _removeMember(String member) {
    setState(() {
      _teamMembers.remove(member);
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: CustomScrollView(
        slivers: [
          SliverAppBar(
            expandedHeight: 165,
            pinned: true,
            floating: true,
            automaticallyImplyLeading: false,
            flexibleSpace: FlexibleSpaceBar(
              titlePadding: const EdgeInsets.only(
                left: 16,
                bottom: 75,
              ),
              centerTitle: false,
              title: Align(
                alignment: Alignment.bottomLeft,
                child: Text(
                  "My Team",
                  style: GoogleFonts.poppins(
                    color: Colors.white,
                    fontSize: 32,
                  ),
                  textAlign: TextAlign.start,
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
                [
                  Text(
                    widget.team.name,
                    style: GoogleFonts.poppins(
                      fontSize: 24,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 8),
                  Text(
                    '${_teamMembers.length}/$_maxTeamSize',
                    style: GoogleFonts.poppins(fontSize: 16),
                  ),
                  const SizedBox(height: 16),
                  Text(
                    'Team Members',
                    style: GoogleFonts.poppins(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 8),
                  if (_teamMembers.isEmpty)
                    const Text('No team members yet.')
                  else
                    ListView.builder(
                      shrinkWrap: true,
                      physics: const NeverScrollableScrollPhysics(),
                      itemCount: _teamMembers.length,
                      itemBuilder: (context, index) {
                        final member = _teamMembers[index];
                        return ListTile(
                          leading:
                              const CircleAvatar(child: Icon(Icons.person)),
                          title: Text(member),
                          trailing: IconButton(
                            icon: const Icon(Icons.close),
                            onPressed: () => _removeMember(member),
                          ),
                        );
                      },
                    ),
                  if (widget.editMode)
                    const SizedBox(height: 8),
                  if (widget.editMode)
                    const Divider(),
                  if (widget.editMode)
                    const SizedBox(height: 8),
                  TeamRequestsView(hunt: widget.hunt, team: widget.team),
                  const SizedBox(height: 16),
                  ElevatedButton(
                    onPressed: () async {
                      if (await _confirmLeaveTeam(context)) {
                        if (!context.mounted) return;
                        Navigator.pop(context);
                      }
                    },
                    style: ElevatedButton.styleFrom(
                      foregroundColor: Colors.white,
                      backgroundColor: praxisRed,
                    ),
                    child: const Text('Leave Team'),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }

  Future<bool> _confirmLeaveTeam(BuildContext context) async {
    return await showDialog(
      context: context,
      builder: (context) => AlertDialog(
        insetPadding: const EdgeInsets.symmetric(vertical: 215),
        backgroundColor: praxisGrey,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(20.0),
          side: const BorderSide(color: Colors.black),
        ),
        title: const Text('Leave Team?'),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.pop(context, true);
            },
            child: const Text('Leave'),
          ),
          TextButton(
            onPressed: () {
              Navigator.pop(context, true);
            },
            child: const Text('Cancel'),
          ),
        ],
      ),
    );
  }
}

class TeamRequestsView extends StatelessWidget {
  final Hunt hunt;
  final Team team;
  final Stream<List<String>> _requests;

  TeamRequestsView({super.key, required this.hunt, required this.team}) : _requests = teamsApi.watchListJoinRequestsForTeam(hunt.id, team.id);

  @override
  Widget build (BuildContext context) {
    return StreamBuilder(
      stream: _requests,
      builder: (context, snapshot) {
        if (!snapshot.hasData) {
          return const Center(child: CircularProgressIndicator());
        } else {
          return Column(
            children: [
              Text(
                'Requests',
                style: GoogleFonts.poppins(
                  fontSize: 18,
                  fontWeight: FontWeight.bold,
                ),
              ),
              const SizedBox(height: 8),
              if (snapshot.data?.isEmpty ?? false)
                const Text(
                  'No pending requests.',
                  style: TextStyle(
                    color: Colors.black,
                  ),
                )
              else
                ListView.builder(
                  shrinkWrap: true,
                  physics: const NeverScrollableScrollPhysics(),
                  itemCount: snapshot.data?.length,
                  itemBuilder: (context, index) {
                    final request = snapshot.data?[index];
                    return ListTile(
                      leading: const CircleAvatar(
                          child: Icon(Icons.person_add)),
                      title: Text(request!),
                      trailing: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          IconButton(
                            icon: const Icon(Icons.check),
                            onPressed: () => _acceptRequest(request),
                          ),
                          IconButton(
                            icon: const Icon(Icons.close),
                            onPressed: () => _rejectRequest(request),
                          ),
                        ],
                      ),
                    );
                  },
                ),
            ],
          );
        }
      },
    );
  }

  void _acceptRequest(String request) async {
    teamsApi.TeamOperationSuccessMessage message = await teamsApi.acceptRequestJoinTeam(hunt.id, team.id, request);
    Fluttertoast.showToast(msg: message.message);
  }

  void _rejectRequest(String request) async {
    teamsApi.TeamOperationSuccessMessage message = await teamsApi.rejectRequestJoinTeam(hunt.id, team.id, request);
    Fluttertoast.showToast(msg: message.message);
  }
}