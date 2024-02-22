import 'package:flutter/material.dart';
import 'package:praxis_afterhours/views/sign_in_view.dart';

class Splash extends StatefulWidget {
  const Splash({super.key});

  @override
  State<Splash> createState() => _SplashState();
}

class _SplashState extends State<Splash> {
  @override
  void initState() {
    super.initState();
    _navigatetoSignIn();
  }

  _navigatetoSignIn() async {
    await Future.delayed(const Duration(seconds: 10));
    Navigator.pushReplacement(
        context, MaterialPageRoute(builder: (context) => SignInView()));
  }

  @override
  Widget build(BuildContext context) {
    return const Scaffold(
      backgroundColor: Color(0xffFFFFFF),
      body: Center(
        child: Stack(
          children: [
            Positioned(
                child: Image(
                    width: 1000,
                    height: 1000,
                    image: AssetImage('../../assets/logo/logo.png'))),
            Positioned(
                bottom: 0,
                right: 0,
                child: Image(
                    width: 200,
                    height: 200,
                    image: AssetImage('../../assets/logo/corner_logo.png'))),
            Positioned(
                bottom: 0,
                left: 0,
                right: 0,
                child: Image(
                    width: 100,
                    height: 100,
                    image: AssetImage('../../assets/logo/copyright.png'))),
          ],
        ),
      ),
    );
  }
}
