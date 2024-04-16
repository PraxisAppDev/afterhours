import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/views/hunt_challenge_screen.dart';

class MockQuestionView extends StatelessWidget {
  const MockQuestionView({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: praxisRed,
        title: Text(
          "Question 1",
          style: GoogleFonts.poppins(
            color: Colors.white,
            fontSize: 35,
          ),
        ),
        actions: [
          IconButton(
            onPressed: () => {},
            icon: const Icon(Icons.person_outline_outlined)
          ),
          IconButton(
            onPressed: () => {},
            icon: const Icon(Icons.timer_sharp)
          ),
          Text(
            "2:36:42",
            style: GoogleFonts.poppins(
              color: Colors.white,
              fontSize: 35,
            )
          ),
        ],
      ),
      body: Column(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "What company's logo is this?",
              style: GoogleFonts.poppins(
                color: Colors.black,
                fontSize: 25,
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Image.asset(
              "images/google.png",
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "Your Answer:",
              style: GoogleFonts.poppins(
                color: Colors.black,
                fontSize: 35,
              )
            ),
          ),
          const Padding(
            padding: EdgeInsets.all(8.0),
            child: TextField(
              decoration: InputDecoration(
                border: OutlineInputBorder(),
                labelText: "Answer Here",
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: TextButton(
              style: ButtonStyle(
                  backgroundColor: const MaterialStatePropertyAll(praxisRed),
                  shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                    RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(3.0),
                      side: const BorderSide(color: praxisRed),
                    ),
                  ),  
              ),
              onPressed: () => {
                challengeSuccessDialog(context)
              },
              child: Text(
                "Submit",
                style: GoogleFonts.poppins(
                  color: Colors.white,
                  fontSize: 40,
                ),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "30 guesses left",
              style: GoogleFonts.poppins(
                color: Colors.black,
                fontSize: 20,
                fontWeight: FontWeight.bold,
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Text(
              "(59 seconds until next guess)",
              style: GoogleFonts.poppins(
                color: Colors.black,
                fontSize: 20,
              ),
            ),
          ),

        ]
      ),
    );
  }

  Future<dynamic> challengeSuccessDialog(BuildContext context) {
    return showDialog(
      context: context,
      builder: (BuildContext context) {
        return Dialog(
          backgroundColor: Colors.white,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(16),
          ),
          child: Column(
            children: <Widget>[
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Text(
                  "Congrats!",
                  style: GoogleFonts.poppins(
                    color: Colors.black,
                    fontSize: 40
                  ),
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(
                  top: 80.0,
                  bottom: 80.0,
                  left: 8.0,
                  right: 8.0,
                ),
                child: Text(
                  "You solved \"Question 1\"!",
                  style: GoogleFonts.poppins(
                    color: Colors.black,
                    fontSize:25
                  ),
                ),
              ),
              const Padding(
                padding: EdgeInsets.all(8.0),
                child: Icon(
                  Icons.check_outlined,
                  color: Colors.green,
                  size: 250,
                ),
              ),
              Padding(
                padding: const EdgeInsets.only(
                  top: 80.0,
                  bottom: 80.0,
                  left: 8.0,
                  right: 8.0,
                ),
                child: TextButton(
                  style: ButtonStyle(
                      // backgroundColor: const MaterialStatePropertyAll(praxisRed),
                      shape: MaterialStateProperty.all<RoundedRectangleBorder>(
                        RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(3.0),
                          side: const BorderSide(color: Colors.black),
                        ),
                      ),  
                  ),
                  onPressed: () => {
                    Navigator.pop(context),
                    Navigator.pop(context),
                  },
                  child: Text(
                    "Back to Problem List",
                    style: GoogleFonts.poppins(
                      color: Colors.black,
                      fontSize: 30,
                    ),
                  ),
                ),
              ),
            ]
          ),
        );
      },
    );
  }
}


// class ChallengeSuccessDialogContent extends StatefulWidget {

//   const JoinHuntOptionsDialogContent({
//     super.key,
//   });

//   @override
//   State<JoinHuntOptionsDialogContent> createState() => _JoinHuntOptionsDialogContentState();
// }

// class _JoinHuntOptionsDialogContentState extends State<JoinHuntOptionsDialogContent> {
//   final TextEditingController newTeamNameController = TextEditingController();

//   @override
//   Widget build(BuildContext context) {
//     return Padding(
//       padding: const EdgeInsets.all(16),
//       child: Column(
//         mainAxisSize: MainAxisSize.min,
//         crossAxisAlignment: CrossAxisAlignment.stretch,
//         children: [
//           Text(
//             'How do you want to join ${widget.hunt.name}?',
//             style: const TextStyle(
//               fontSize: 18,
//               fontWeight: FontWeight.bold,
//             ),
//           ),
//           const SizedBox(height: 16),
//           OpenContainer(
//             useRootNavigator: true,
//             transitionDuration: const Duration(seconds: 1),
//             openBuilder: (context, _) => JoinTeamView(huntId: widget.hunt.id),
//             closedShape: RoundedRectangleBorder(
//               borderRadius: BorderRadius.circular(8),
//             ),
//             closedColor: Colors.transparent,
//             closedBuilder: (context, _) => Container(
//               color: praxisRed,
//               child: const Padding(
//                 padding: EdgeInsets.symmetric(vertical: 16),
//                 child: Text(
//                   'Join Team',
//                   style: TextStyle(
//                     fontSize: 16,
//                     color: Colors.white,
//                   ),
//                   textAlign: TextAlign.center,
//                 ),
//               ),
//             ),
//           ),
//           const SizedBox(height: 16),
//           GestureDetector(
//             onTap: () {
//               //close this dialog and open a new one to enter a team name
//               Navigator.pop(context);
//               showDialog(
//                 context: context,
//                 builder: (BuildContext context) {
//                   return Dialog(
//                     backgroundColor: Colors.white,
//                     shape: RoundedRectangleBorder(
//                       borderRadius: BorderRadius.circular(16),
//                     ),
//                     child: Padding(
//                       padding: const EdgeInsets.all(16),
//                       child: Column(
//                         mainAxisSize: MainAxisSize.min,
//                         crossAxisAlignment: CrossAxisAlignment.stretch,
//                         children: [
//                           const Text(
//                             'Enter a team name',
//                             style: TextStyle(
//                               fontSize: 18,
//                               fontWeight: FontWeight.bold,
//                             ),
//                           ),
//                           const SizedBox(height: 16),
//                           TextField(
//                             decoration: const InputDecoration(
//                               hintText: 'Team Name',
//                             ),
//                             controller: newTeamNameController,
//                           ),
//                           const SizedBox(height: 16),
//                           OpenContainer(
//                             transitionDuration:
//                             const Duration(seconds: 1),
//                             openBuilder: (context, _) => CreateTeamView(hunt: widget.hunt, initialTeamName: newTeamNameController.text),
//                             closedShape: RoundedRectangleBorder(
//                               borderRadius: BorderRadius.circular(8),
//                             ),
//                             closedColor: Colors.transparent,
//                             closedBuilder: (context, _) => Container(
//                               color: praxisRed,
//                               child: const Padding(
//                                 padding:
//                                 EdgeInsets.symmetric(vertical: 16),
//                                 child: Text(
//                                   'Create Team',
//                                   style: TextStyle(
//                                     fontSize: 16,
//                                     color: Colors.white,
//                                   ),
//                                   textAlign: TextAlign.center,
//                                 ),
//                               ),
//                             ),
//                           ),
//                         ],
//                       ),
//                     ),
//                   );
//                 },
//               );
//             },
//             child: Container(
//               decoration: BoxDecoration(
//                 borderRadius: BorderRadius.circular(8),
//                 color: praxisRed,
//               ),
//               child: const Padding(
//                 padding: EdgeInsets.symmetric(vertical: 16),
//                 child: Text(
//                   'Create Team',
//                   style: TextStyle(
//                     color: Colors.white,
//                     fontSize: 16,
//                   ),
//                   textAlign: TextAlign.center,
//                 ),
//               ),
//             ),
//           ),
//           const SizedBox(height: 16),
//           OpenContainer(
//             useRootNavigator: true,
//             transitionDuration: const Duration(seconds: 1),
//             openBuilder: (context, _) => const GetReadyHuntView(),
//             closedShape: RoundedRectangleBorder(
//               borderRadius: BorderRadius.circular(8),
//             ),
//             closedColor: Colors.transparent,
//             closedBuilder: (context, _) => Container(
//               color: praxisRed,
//               child: const Padding(
//                 padding: EdgeInsets.symmetric(vertical: 16),
//                 child: Text(
//                   'Hunt Alone',
//                   style: TextStyle(
//                     color: Colors.white,
//                     fontSize: 16,
//                   ),
//                   textAlign: TextAlign.center,
//                 ),
//               ),
//             ),
//           ),
//         ],
//       ),
//     );
//   }
// }