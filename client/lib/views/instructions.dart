import 'package:flutter/material.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class Instructions extends StatelessWidget {
  const Instructions({super.key, required this.title});
  final String title;
  final EdgeInsets margins = const EdgeInsets.all(32.0);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        color: praxisRed,
        child: Stack(
          children: [
            Positioned(
              top: 0,
              left: 0,
              right: 0,
              bottom: 0,
              child: Padding(
                padding: margins,
                child: SingleChildScrollView(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(
                        children: [
                          IconButton(
                            onPressed: () {
                              Navigator.pop(context);
                            },
                            icon: const Icon(Icons.arrow_back,
                                color: praxisBlack, size: 30),
                          ),
                          const SizedBox(
                              width:
                                  8), //spacing between the back button and the "How to Play" text
                          const Flexible(
                            fit: FlexFit.loose, //prevent overflow error
                            child: Text(
                              'How to Play',
                              textAlign: TextAlign.center,
                              style: TextStyle(
                                fontSize: 35,
                                fontWeight: FontWeight.bold,
                                color: praxisWhite,
                              ),
                              overflow: TextOverflow
                                  .ellipsis, //prevent overflow error
                            ),
                          ),
                        ],
                      ),
                      const SizedBox(
                          height:
                              20), //spacing between "How to Play" text and other text
                      const Text(
                        'Welcome to AFTERHOURS Hunts – where participants, either individuals or teams, attempt to solve a series of intriguing  challenges while delving deeper into the world of Praxis. Pool your diverse talents, strategize together, and unleash your creativity to conquer each challenge that lies ahead.\n',
                        textAlign: TextAlign.center,
                        style: TextStyle(fontSize: 20, color: praxisWhite),
                      ),
                      const Divider(
                          color:
                              praxisWhite), //adding divider(line) between intro and instructions
                      const Text(
                        '\n1. Each challenge presents a unique puzzle to solve. Work together to find the solution, but remember, you only have a limited number of guesses per challenge. Additionally, a timer will determine when you can make your next attempt.\n\n'
                        '2. Find detailed instructions for each challenge on its respective page.\n\n'
                        '3. Keep an eye on the leaderboard by clicking the three bars. See how your team stacks up against the competition and track your progress throughout the Hunt.\n\n'
                        '4. Should you find yourselves in need of guidance, do not hesitate to seek help from your fellow participants or the Praxis employees overseeing the event. They are here to support you on your quest.\n\n'
                        '5. Get ready to embark on an adventure like no other.\n\n'
                        'Happy Hunting!',
                        textAlign: TextAlign.left,
                        style: TextStyle(fontSize: 20, color: praxisWhite),
                      ),
                    ],
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
