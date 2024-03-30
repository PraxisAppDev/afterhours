import 'package:intl/intl.dart';

class HuntLocation {
  final String type;
  final String locationName;
  final String locationInstructions;
  final Geofence geofence;

  HuntLocation({
    required this.type,
    required this.locationName,
    required this.locationInstructions,
    required this.geofence,
  });

  factory HuntLocation.fromJson(Map<String, dynamic> json) {
    return HuntLocation(
      type: json['type'],
      locationName: json['locationName'],
      locationInstructions: json['locationInstructions'],
      geofence: Geofence.fromJson(json['geofence']),
    );
  }
}

class Geofence {
  final String type;
  final List<double> coordinates;
  final double radius;

  Geofence({
    required this.type,
    required this.coordinates,
    required this.radius,
  });

  factory Geofence.fromJson(Map<String, dynamic> json) {
    return Geofence(
      type: json['type'],
      coordinates: List<double>.from(json['coordinates']),
      radius: json['radius'],
    );
  }
}

class Challenge {
  final String questionTitle;
  final String description;
  final String imageURL;
  final String placeholderText;
  final Sequence sequence;
  final List<Hint> hints;
  final Scoring scoring;
  final Response response;

  Challenge({
    required this.questionTitle,
    required this.description,
    required this.imageURL,
    required this.placeholderText,
    required this.sequence,
    required this.hints,
    required this.scoring,
    required this.response,
  });

  factory Challenge.fromJson(Map<String, dynamic> json) {
    return Challenge(
      questionTitle: json['questionTitle'],
      description: json['description'],
      imageURL: json['imageURL'],
      placeholderText: json['placeholderText'],
      sequence: Sequence.fromJson(json['sequence']),
      hints: List<Hint>.from(json['hints'].map((hint) => Hint.fromJson(hint))),
      scoring: Scoring.fromJson(json['scoring']),
      response: Response.fromJson(json['response']),
    );
  }
}

class Sequence {
  final int num;
  final int order;

  Sequence({
    required this.num,
    required this.order,
  });

  factory Sequence.fromJson(Map<String, dynamic> json) {
    return Sequence(
      num: json['num'],
      order: json['order'],
    );
  }
}

class Hint {
  final String type;
  final double penalty;
  final String text;

  Hint({
    required this.type,
    required this.penalty,
    required this.text,
  });

  factory Hint.fromJson(Map<String, dynamic> json) {
    return Hint(
      type: json['type'],
      penalty: json['penalty'],
      text: json['text'],
    );
  }
}

class Scoring {
  final double points;
  final TimeDecay timeDecay;

  Scoring({
    required this.points,
    required this.timeDecay,
  });

  factory Scoring.fromJson(Map<String, dynamic> json) {
    return Scoring(
      points: json['points'],
      timeDecay: TimeDecay.fromJson(json['timeDecay']),
    );
  }
}

class TimeDecay {
  final String type;
  final int? timeLimit;

  TimeDecay({
    required this.type,
    this.timeLimit,
  });

  factory TimeDecay.fromJson(Map<String, dynamic> json) {
    return TimeDecay(
      type: json['type'],
      timeLimit: json['timeLimit'],
    );
  }
}

class Response {
  final String type;
  final List<String> possibleAnswers;
  final bool caseSensitive;

  Response({
    required this.type,
    required this.possibleAnswers,
    required this.caseSensitive,
  });

  factory Response.fromJson(Map<String, dynamic> json) {
    return Response(
      type: json['type'],
      possibleAnswers: List<String>.from(json['possibleAnswers']),
      caseSensitive: json['caseSensitive'],
    );
  }
}

class Hunt {
  final String id;
  final String name;
  final String description;
  final DateTime startDate;
  final DateTime joinableAfterDate;
  final DateTime endDate;
  final HuntLocation huntLocation;
  final List<Challenge> challenges;

  Hunt({
    required this.id,
    required this.name,
    required this.description,
    required this.startDate,
    required this.joinableAfterDate,
    required this.endDate,
    required this.huntLocation,
    required this.challenges,
  });

  factory Hunt.fromJson(Map<String, dynamic> json) {
    return Hunt(
      id: json['_id'],
      name: json['name'],
      description: json['description'],
      startDate: _parseDate(json['startDate']),
      joinableAfterDate: _parseDate(json['joinableAfterDate']),
      endDate: _parseDate(json['endDate']),
      huntLocation: HuntLocation.fromJson(json['huntLocation']),
      challenges: List<Challenge>.from(
          json['challenges'].map((challenge) => Challenge.fromJson(challenge))),
    );
  }

  static DateTime _parseDate(String dateString) {
    final formatter = DateFormat('yyyy-MM-dd hh:mm a');
    return formatter.parse(dateString);
  }
}
