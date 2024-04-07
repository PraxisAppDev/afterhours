import 'package:intl/intl.dart';
import 'package:json_annotation/json_annotation.dart';

part 'hunt_structure.g.dart';

@JsonSerializable()
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

  factory HuntLocation.fromJson(Map<String, dynamic> json) => _$HuntLocationFromJson(json);

  Map<String, dynamic> toJson() => _$HuntLocationToJson(this);
}

@JsonSerializable()
class Geofence {
  final String type;
  final List<double> coordinates;
  final double radius;

  Geofence({
    required this.type,
    required this.coordinates,
    required this.radius,
  });

  factory Geofence.fromJson(Map<String, dynamic> json) => _$GeofenceFromJson(json);

  Map<String, dynamic> toJson() => _$GeofenceToJson(this);
}

@JsonSerializable()
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

  factory Challenge.fromJson(Map<String, dynamic> json) => _$ChallengeFromJson(json);
}

@JsonSerializable()
class Sequence {
  final int num;
  final int order;

  Sequence({
    required this.num,
    required this.order,
  });

  factory Sequence.fromJson(Map<String, dynamic> json) => _$SequenceFromJson(json);

  Map<String, dynamic> toJson() => _$SequenceToJson(this);
}

@JsonSerializable()
class Hint {
  final String type;
  final double penalty;
  final String text;

  Hint({
    required this.type,
    required this.penalty,
    required this.text,
  });

  factory Hint.fromJson(Map<String, dynamic> json) => _$HintFromJson(json);

  Map<String, dynamic> toJson() => _$HintToJson(this);
}

@JsonSerializable()
class Scoring {
  final double points;
  final TimeDecay timeDecay;

  Scoring({
    required this.points,
    required this.timeDecay,
  });

  factory Scoring.fromJson(Map<String, dynamic> json) => _$ScoringFromJson(json);

  Map<String, dynamic> toJson() => _$ScoringToJson(this);
}

@JsonSerializable()
class TimeDecay {
  final String type;
  final int? timeLimit;

  TimeDecay({
    required this.type,
    this.timeLimit,
  });

  factory TimeDecay.fromJson(Map<String, dynamic> json) => _$TimeDecayFromJson(json);
}

@JsonSerializable()
class Response {
  final String type;
  final List<String> possibleAnswers;
  final bool caseSensitive;

  Response({
    required this.type,
    required this.possibleAnswers,
    required this.caseSensitive,
  });

  factory Response.fromJson(Map<String, dynamic> json) => _$ResponseFromJson(json);
}

@JsonSerializable()
class Hunt {
  @JsonKey(name: '_id')
  final String id;
  final String name;
  final String description;
  @JsonKey(fromJson: _DateUtil._fromJson, toJson: _DateUtil._toJson)
  final DateTime startDate;
  @JsonKey(fromJson: _DateUtil._fromJsonNullable, toJson: _DateUtil._toJsonNullable)
  final DateTime? joinableAfterDate;
  @JsonKey(fromJson: _DateUtil._fromJson, toJson: _DateUtil._toJson)
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

  factory Hunt.fromJson(Map<String, dynamic> json) => _$HuntFromJson(json);

  Map<String, dynamic> toJson() => _$HuntToJson(this);
}

class _DateUtil {
  static final formatter = DateFormat('yyyy-MM-dd hh:mm a');

  static DateTime _fromJson(String date) {
    return formatter.parse(date);
  }

  static String _toJson(DateTime date) {
    return formatter.format(date);
  }

  static DateTime? _fromJsonNullable(String? date) {
    return (date?.isEmpty ?? true) ? null : formatter.parse(date!);
  }

  static String _toJsonNullable(DateTime? date) {
    return date == null ? '' : formatter.format(date);
  }
}

class Team {
  final String id;
  final String name;
  String teamLeader;
  List<String> players;
  List<String> invitations;
  final int capacity;
  bool isLocked;

  Team({
    required this.id,
    required this.name,
    required this.teamLeader,
    required this.players,
    required this.invitations,
    required this.capacity,
    required this.isLocked,
  });

  factory Team.fromJson(Map<String, dynamic> json) {
    return Team(
      id: json['hunt_id'],
      name: json['name'],
      teamLeader: json['teamLead'],
      players: List<String>.from(json['players']),
      invitations: List<String>.from(json['invitations']),
      capacity: json['capacity'],
      isLocked: json['isLocked'],
    );
  }

}
