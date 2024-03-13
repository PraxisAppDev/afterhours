import 'package:praxis_afterhours/entities/challenge.dart';

class UpcomingHunt {
  final String title;
  final String date;
  final String location;
  final String locationInstructions;
  final List<double> coordinates;
  final double geoFenceRadius;
  final List<Challenge> challenges;
  final String trailing;

  const UpcomingHunt({
    required this.title,
    required this.location,
    required this.date,
    required this.locationInstructions,
    required this.coordinates,
    required this.geoFenceRadius,
    required this.challenges,
    this.trailing = '',
  });

  @override
  String toString() {
    return "{$title, $location, $date, $locationInstructions, $coordinates, $geoFenceRadius}";
  }

  factory UpcomingHunt.fromJson(Map<String, dynamic> json) {
    return UpcomingHunt(
      title: json["name"],
      location: json["huntLocation"]["locationName"],
      date: json["startDate"],
      locationInstructions: json["huntLocation"]["locationInstructions"],
      coordinates: json["huntLocation"]["geofence"]["coordinates"]
          .map<double>((coord) => double.parse(coord.toString()))
          .toList(),
      geoFenceRadius: json["huntLocation"]["geofence"]["radius"],
      challenges: json["challenges"]
          .map<Challenge>((challenge) => Challenge.fromJson(challenge))
          .toList(),
    );
  }
}
