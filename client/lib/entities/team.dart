class Team {
  final String teamName;
  final List teamMembers;
  final String capacity;
  final bool isFull;
  final String reasonFull;

  const Team({
    required this.teamName,
    required this.teamMembers,
    required this.capacity,
    required this.isFull,
    required this.reasonFull,
  });

  factory Team.fromJson(Map<String, dynamic> json) {
    return switch (json) {
      {
        "team_name": String teamName,
        "team_members": List teamMembers,
        "capacity": String capacity,
        "is_full": String isFull,
        "reason_full": String reasonFull,
      } =>
        Team(
          teamName: teamName,
          teamMembers: teamMembers,
          capacity: capacity,
          isFull: isFull == "true" ? true : false,
          reasonFull: reasonFull,
        ),
      _ => throw const FormatException(
          "Failed to load available teams. : team.dart")
    };
  }
}
