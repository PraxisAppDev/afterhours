// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'web_socket_channel.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

InitRequestMessage _$InitRequestMessageFromJson(Map<String, dynamic> json) =>
    InitRequestMessage(
      teamId: json['teamId'] as String,
      authToken: json['authToken'] as String,
      role: $enumDecode(_$TeamInitRoleEnumMap, json['role']),
      protocolExtensions: (json['protocolExtensions'] as List<dynamic>?)
              ?.map((e) => e as String)
              .toList() ??
          const [],
    );

Map<String, dynamic> _$InitRequestMessageToJson(InitRequestMessage instance) =>
    <String, dynamic>{
      'teamId': instance.teamId,
      'authToken': instance.authToken,
      'role': _$TeamInitRoleEnumMap[instance.role]!,
      'protocolExtensions': instance.protocolExtensions,
    };

const _$TeamInitRoleEnumMap = {
  TeamInitRole.teamLeader: 'TEAM_LEADER',
  TeamInitRole.teamJoiner: 'TEAM_JOINER',
};

InitResponseMessage _$InitResponseMessageFromJson(Map<String, dynamic> json) =>
    InitResponseMessage(
      success: json['success'] as bool,
      errorMessage:
          $enumDecodeNullable(_$TeamErrorMessageEnumMap, json['errorMessage']),
    );

Map<String, dynamic> _$InitResponseMessageToJson(
        InitResponseMessage instance) =>
    <String, dynamic>{
      'success': instance.success,
      'errorMessage': _$TeamErrorMessageEnumMap[instance.errorMessage],
    };

const _$TeamErrorMessageEnumMap = {
  TeamErrorMessage.invalidRequest: 'INVALID_REQUEST',
  TeamErrorMessage.invalidToken: 'INVALID_TOKEN',
  TeamErrorMessage.upgradeApiVersion: 'UPGRADE_API_VERSION',
  TeamErrorMessage.invalidApiVersion: 'INVALID_API_VERSION',
  TeamErrorMessage.tooManyConnections: 'TOO_MANY_CONNECTIONS',
};

TeamJoinRequestMessage _$TeamJoinRequestMessageFromJson(
        Map<String, dynamic> json) =>
    TeamJoinRequestMessage(
      teamId: json['teamId'] as String,
      userId: json['userId'] as String,
    );

Map<String, dynamic> _$TeamJoinRequestMessageToJson(
        TeamJoinRequestMessage instance) =>
    <String, dynamic>{
      'teamId': instance.teamId,
      'userId': instance.userId,
    };
