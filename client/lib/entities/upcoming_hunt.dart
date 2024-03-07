class UpcomingHunt {
  final String title;
  final String date;
  final String location;
  final String trailing;

  const UpcomingHunt({
    required this.title,
    required this.location,
    required this.date,
    this.trailing = '',
  });

  @override
  String toString() {
    return "{$title, $location, $date}";
  }

  factory UpcomingHunt.fromJson(Map<String, dynamic> json) {
    return switch (json) {
      {
        "title": String title,
        "location": String location,
        "date": String date,
      } =>
        UpcomingHunt(
          title: title,
          location: location,
          date: date,
        ),
      _ => throw const FormatException("Failed to load upcoming hunts.")
    };
  }
}
