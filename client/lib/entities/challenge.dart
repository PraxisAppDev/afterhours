import 'package:praxis_afterhours/entities/hint.dart';

class Challenge {
  final String questionTitle;
  final String description;
  final String imageURL;
  final String placeholderText;
  final int sequenceNum;
  final int sequenceOrder;
  final List<Hint> hints;
  final double points;
  final String timeDecayType;
  final String responseType;
  final List<String> possibleAnswers;
  final bool caseSensitive;

  const Challenge({
    required this.questionTitle,
    required this.description,
    required this.imageURL,
    required this.placeholderText,
    required this.sequenceNum,
    required this.sequenceOrder,
    required this.hints,
    required this.points,
    required this.timeDecayType,
    required this.responseType,
    required this.possibleAnswers,
    required this.caseSensitive,
  });

  factory Challenge.fromJson(Map<String, dynamic> json) {
    return Challenge(
      questionTitle: json["questionTitle"],
      description: json["description"],
      imageURL: json["imageURL"],
      placeholderText: json["placeholderText"],
      sequenceNum: json["sequence"]["num"],
      sequenceOrder: json["sequence"]["order"],
      hints: json["hints"].map<Hint>((hint) => Hint.fromJson(hint)).toList(),
      points: json["scoring"]["points"],
      timeDecayType: json["scoring"]["timeDecay"]["type"],
      responseType: json["response"]["type"],
      possibleAnswers: json["response"]["possibleAnswers"]
          .map<String>((ans) => ans.toString())
          .toList(),
      caseSensitive: json["response"]["caseSensitive"],
    );
  }
}
