import 'package:flutter/material.dart';
import 'package:praxis_afterhours/constants/colors.dart';

class HuntChallengeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          // Background white container
          Container(
            color: Colors.white,
            height: MediaQuery.of(context).size.height,
            width: MediaQuery.of(context).size.width,
          ),
          // Positioned container with specified properties (green)
          Positioned(
            top: 370,
            left: 99,
            width: 276,
            height: 103,
            child: Container(
              decoration: BoxDecoration(
                color: Color(0xFF117120), 
                borderRadius: BorderRadius.circular(15),
              ),
            ),
          ),
          // Positioned container with specified properties (red)
          Positioned(
            top: 502,
            left: 99,
            width: 276,
            height: 103,
            child: Container(
              decoration: BoxDecoration(
                color: praxisRed, 
                borderRadius: BorderRadius.circular(15), 
              ),
            ),
          ),
          // Positioned container with specified properties (additional red)
          Positioned(
            top: 1,
            left: 0,
            width: 430,
            height: 313,
            child: Container(
              color: praxisRed, 
            ),
          ),
          // Positioned container with specified properties (gray)
          Positioned(
            top: 640,
            left: 99,
            width: 276,
            height: 103,
            child: Container(
              decoration: BoxDecoration(
                color: Color(0xFFD9D9D9), 
                borderRadius: BorderRadius.circular(15), 
              ),
            ),
          ),
          // Positioned container with specified properties (additional gray)
          Positioned(
            top: 772,
            left: 99,
            width: 276,
            height: 103,
            child: Container(
              decoration: BoxDecoration(
                color: Color(0xFFD9D9D9), 
                borderRadius: BorderRadius.circular(15), 
              ),
            ),
          ),
          // Positioned container with specified properties (leaderboard icon)
          Positioned(
            top: 129, 
            left: 297, 
            width: 43,
            height: 39,
            child: Container(
              decoration: BoxDecoration(
                
              ),
              child: Icon(
                Icons.leaderboard, 
                size: 39, 
                color: Colors.white, 
              ),
            ),
          ),
          // Positioned container with specified properties (schedule icon)
          Positioned(
            top: 191, 
            left: 30, 
            width: 36,
            height: 42,
            child: Container(
              decoration: BoxDecoration(
                
              ),
              child: Icon(
                Icons.schedule, 
                size: 36, 
                color: Colors.white,
              ),
            ),
          ),
          // Positioned container with specified properties (score icon)
          Positioned(
            top: 243, 
            left: 30,
            width: 36,
            height: 36,
            child: Container(
              decoration: BoxDecoration(
                
              ),
              child: Icon(
                Icons.score,
                size: 36, 
                color: Colors.white, 
               
              ),
            ),
          ),
          // Positioned container with specified properties (person icon)
          Positioned(
            top: 130.17, 
            left: 358.17, 
            width: 36.67,
            height: 36.67,
            child: Container(
              decoration: BoxDecoration(
                
              ),
              child: Icon(
                Icons.person, 
                size: 36.67, 
                color: Colors.white, 
              ),
            ),
          ),
          // Positioned container with specified properties (text: Recruit Mixer)
          Positioned(
            top: 140, 
            left: 30, 
            width: 211,
            height: 35,
            child: Text(
              "Recruit Mixer",
               style: TextStyle(
                fontFamily: 'Josefin Sans', 
                fontSize: 35, 
                fontWeight: FontWeight.w400, 
                color: Colors.white, 
                height: 1, 
                letterSpacing: 0, 
              ),
              textAlign: TextAlign.left,
            ),
          ),
          // Positioned container with specified properties (text: "36:42 left")
          Positioned(
            top: 198,
            left: 82,
            width: 180,
            height: 35,
            child: Text(
              "36:42 left",
              style: TextStyle(
                fontFamily: 'Josefin Sans',
                fontSize: 35,
                fontWeight: FontWeight.w400,
                color: Colors.white,
                height: 1,
                letterSpacing: 0,
              ),
              textAlign: TextAlign.left,
              ),
          ),
          // Positioned container with specified properties (text: "200 points")
          Positioned(
            top: 243,
            left: 82,
            width: 169,
            height: 35,
            child: Text(
              "200 points",
              style: TextStyle(
                fontFamily: 'Josefin Sans',
                fontSize: 35,
                fontWeight: FontWeight.w400,
                color: Colors.white,
                height: 1,
                letterSpacing: 0,
             ),
              textAlign: TextAlign.left,
            ),
          ),
          // Positioned container with specified properties (schedule icon)
            Positioned(
              top: 426,
              left: 119,
              width: 18,
              height: 21,
              child: Container(
                decoration: BoxDecoration(
                  
                ),
                child: Icon(
                  Icons.schedule, 
                  size: 18, 
                  color: Colors.white,
                ),
            ),
          ),
          // Positioned container with specified properties (score icon)
            Positioned(
              top: 427,
              left: 210,
              width: 19,
              height: 18,
              child: Container(
                decoration: BoxDecoration(
                  
                ),
                child: Icon(
                  Icons.score, 
                  size: 19, 
                  color: Colors.white,
                ),
              ),
            ),
            // Positioned container with specified properties (text: "9:34 200 points")
              Positioned(
                top: 426,
                left: 145,
                width: 217,
                height: 21,
                child: Text(
                  "9:34       200 points",
                  style: TextStyle(
                    fontFamily: 'Josefin Sans',
                    fontSize: 25,
                    fontWeight: FontWeight.w400,
                    color: Colors.white,
                    height: 1,
                    letterSpacing: 0,
                  ),
                  textAlign: TextAlign.left,
                ),
              ),
              // Positioned container with specified properties (text: "Challenge 1")
                Positioned(
                  top: 391,
                  left: 120,
                  width: 150,
                  height: 25,
                  child: Text(
                    "Challenge 1",
                    style: TextStyle(
                      fontFamily: 'Josefin Sans',
                      fontSize: 25,
                      fontWeight: FontWeight.w400,
                      color: Colors.white,
                      height: 1,
                      letterSpacing: 0,
                    ),
                    textAlign: TextAlign.left,
                  ),
                ),

                // creates the line to connect the challenges (line red)
                Positioned(
                  top: 421,
                  left: 62,
                  height: 134,
                  width: 3,
                    child: Container(
                      color: Colors.red,
                    ),
                  ),
                  // Positioned container with specified properties (line gray)
                    Positioned(
                      top: 564,
                      left: 62,
                      height: 268,
                      width: 3,
                      child: Container(
                        color: Color(0xFFD9D9D9),
                      ),
                    ),

               // creates the circle to connect the challenges 
                Positioned(
                  top: 413,
                  left: 55,
                  width: 18,
                  height: 18,
                  child: Container(
                    decoration: BoxDecoration(
                      color: praxisRed,
                      shape: BoxShape.circle,
                    ),
                  ),
                ),
                // creates the circle to connect the challenges 
                Positioned(
                  top: 546,
                  left: 55,
                  width: 18,
                  height: 18,
                  child: Container(
                    decoration: BoxDecoration(
                      color: praxisRed,
                      shape: BoxShape.circle,
                    ),
                  ),
                ), 
                // creates gray circle for a new challenge
                Positioned(
                  top: 684,
                  left: 55,
                  width: 18,
                  height: 18,
                  child: Container(
                    decoration: BoxDecoration(
                      color: Color(0xFFD9D9D9),
                      shape: BoxShape.circle,
                    ),
                  ),
                ),
                // creates gray circle 
                Positioned(
                  top: 684,
                  left: 55,
                  width: 18,
                  height: 18,
                  child: Container(
                    decoration: BoxDecoration(
                      color: Color(0xFFD9D9D9),
                      shape: BoxShape.circle,
                    ),
                  ),
                ), 
                // creates gray circle 
                Positioned(
                  top: 818,
                  left: 55,
                  width: 18,
                  height: 18,
                  child: Container(
                    decoration: BoxDecoration(
                      color: Color(0xFFD9D9D9),
                      shape: BoxShape.circle,
                    ),
                  ),
                ),         
                // Positioned container with specified properties (lock icon)
                  Positioned(
                    top: 672,
                    left: 227,
                    width: 20,
                    height: 27,
                    child: Icon(
                      Icons.lock,
                      color: Colors.white,
                    ),
                  ),
                  // Positioned container with specified properties (arrow back icon)
                    Positioned(
                      top: 85,
                      left: 25,
                      width: 40,
                      height: 41,
                      child: Icon(
                        Icons.arrow_back,
                        color: Colors.white,
                        size: 40,
                      ),
                    ),
        ],
      ),
    );
  }
}
