import 'package:flutter/material.dart';
import 'package:praxis_afterhours/constants/colors.dart';
import 'package:praxis_afterhours/views/join_hunt_view.dart';

class BottomNavBar extends StatefulWidget {
  const BottomNavBar({super.key});

  @override
  State<BottomNavBar> createState() => _BottomNavBarState();
}

class _BottomNavBarState extends State<BottomNavBar> {
  int currentPageIndex = 0;
  final screens = [
    const JoinHuntView(),
    const Text("History"),
    const Text("Profile"),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: screens[currentPageIndex],
      bottomNavigationBar: NavigationBar(
        onDestinationSelected: (int index) {
          setState(() {
            currentPageIndex = index;
          });
        },
        indicatorColor: praxisRed,
        selectedIndex: currentPageIndex,
        destinations: const [
          NavigationDestination(
            icon: Icon(Icons.play_arrow),
            label: "Join a Hunt",
          ),
          NavigationDestination(
            icon: Icon(Icons.history),
            label: "History",
          ),
          NavigationDestination(
            icon: Icon(Icons.person),
            label: "Profile",
          )
        ],
      ),
    );
  }
}
