// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'teams_api.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

TeamsResponseModel _$TeamsResponseModelFromJson(Map<String, dynamic> json) =>
    TeamsResponseModel(
      message: json['message'] as String,
      teams: (json['teams'] as List<dynamic>)
          .map((e) => TeamModel.fromJson(e as Map<String, dynamic>))
          .toList(),
    );

Map<String, dynamic> _$TeamsResponseModelToJson(TeamsResponseModel instance) =>
    <String, dynamic>{
      'message': instance.message,
      'teams': instance.teams,
    };

TeamModel _$TeamModelFromJson(Map<String, dynamic> json) => TeamModel(
      huntId: json['hunt_id'] as String,
      teamName: json['name'] as String,
      teamLead: json['teamLead'] as String,
      playerIds:
          (json['playerIds'] as List<dynamic>).map((e) => e as String).toList(),
      challengeResults: (json['challengeResults'] as List<dynamic>)
          .map((e) => e as String)
          .toList(),
      invitations: (json['invitations'] as List<dynamic>)
          .map((e) => e as String)
          .toList(),
    );

Map<String, dynamic> _$TeamModelToJson(TeamModel instance) => <String, dynamic>{
      'hunt_id': instance.huntId,
      'name': instance.teamName,
      'teamLead': instance.teamLead,
      'playerIds': instance.playerIds,
      'challengeResults': instance.challengeResults,
      'invitations': instance.invitations,
    };
