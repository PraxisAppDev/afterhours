class Hint {
  final double penalty;
  final String text;

  const Hint({
    required this.penalty,
    required this.text,
  });

  factory Hint.fromJson(Map<String, dynamic> json) {
    return Hint(
      penalty: json["penalty"],
      text: json["text"],
    );
  }
}
