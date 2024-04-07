import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class CreateTeamView extends StatefulWidget {
  const CreateTeamView({super.key});

  @override
  State<CreateTeamView> createState() => _CreateTeamViewState();
}

class _CreateTeamViewState extends State<CreateTeamView> {
  final TextEditingController _teamNameController = TextEditingController();
  final List<String> _teamMembers = ['Chell', 'GLaDOS', 'Wheatley'];
  final List<String> _requests = ['NewMember1', 'NewMember2', 'NewMember3'];
  final int _maxTeamSize = 4;

  @override
  void dispose() {
    _teamNameController.dispose();
    super.dispose();
  }

  void _removeMember(String member) {
    setState(() {
      _teamMembers.remove(member);
    });
  }

  void _acceptRequest(String request) {
    setState(() {
      if (_teamMembers.length < _maxTeamSize) {
        _teamMembers.add(request);
        _requests.remove(request);
      }
    });
  }

  void _rejectRequest(String request) {
    setState(() {
      _requests.remove(request);
    });
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
                    'Aperture Science',
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
                  const SizedBox(height: 16),
                  Text(
                    'Requests',
                    style: GoogleFonts.poppins(
                      fontSize: 18,
                      fontWeight: FontWeight.bold,
                    ),
                  ),
                  const SizedBox(height: 8),
                  if (_requests.isEmpty)
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
                      itemCount: _requests.length,
                      itemBuilder: (context, index) {
                        final request = _requests[index];
                        return ListTile(
                          leading:
                              const CircleAvatar(child: Icon(Icons.person_add)),
                          title: Text(request),
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
                  const SizedBox(height: 16),
                  ElevatedButton(
                    onPressed: () {
                      // TODO: Implement leaving the team
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
}
