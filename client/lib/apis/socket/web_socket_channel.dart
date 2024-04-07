import 'dart:convert';

import 'package:flutter/foundation.dart';
import 'package:web_socket_channel/web_socket_channel.dart';
import 'package:json_annotation/json_annotation.dart';

part 'web_socket_channel.g.dart';

class JSONWebsocketChannel {
  final WebSocketChannel _channel;

  JSONWebsocketChannel(Uri url) : _channel = WebSocketChannel.connect(url);

  Future<void> get ready => _channel.ready;

  Stream<ResponseMessageBase> getStream() => _channel.stream.map((streamObject) {
    return ResponseMessageBase.fromJson(jsonDecode(streamObject));
  });

  void send(RequestMessageBase message) {
    _channel.sink.add(jsonEncode(message.toJson()));
  }
}

class WebSocketApiRequest {
  final JSONWebsocketChannel _channel;
  late final Stream<ResponseMessageBase> _responseStream;

  String teamId;
  String authToken;
  TeamInitRole role;

  WebSocketApiRequest(Uri uri, {required this.teamId, required this.authToken, required this.role})
   : _channel = JSONWebsocketChannel(uri) {
    _responseStream = _createResponseStream();
  }

  Stream<ResponseMessageBase> _createResponseStream() async* {
    await _channel.ready;
    _channel.send(InitRequestMessage(
        teamId: teamId,
        authToken: authToken,
        role: role
    ));
    Stream<ResponseMessageBase> responseStream = _channel.getStream();
    ResponseMessageBase firstResponse = await responseStream.first;
    if (kDebugMode) {
      print(firstResponse);
    }
    if(firstResponse is! InitResponseMessage) {
      throw Exception('Failed to initialize connection: $firstResponse is of an invalid type');
    }
    InitResponseMessage initResponse = firstResponse;
    if(!initResponse.success) {
      throw Exception('Failed to initialize connection: ${initResponse.errorMessage}');
    }

    yield* responseStream;
  }

  Stream<ResponseMessageBase> get responseStream async* {
    yield* _responseStream;
  }
}

@JsonEnum()
enum TeamRequestType {
  @JsonValue("TEAM_JOIN_REQUEST")
  teamJoinRequest,
  @JsonValue("TEAM_ACCEPT_REQUEST")
  teamAcceptRequest,
  @JsonValue("TEAM_REJECT_REQUEST")
  teamRejectRequest;
}

@JsonEnum()
enum TeamResponseType {
  @JsonValue("TEAM_JOIN_RESPONSE")
  teamJoinResponse,
  @JsonValue("TEAM_ACCEPT_RESPONSE")
  teamAcceptResponse,
  @JsonValue("TEAM_REJECT_RESPONSE")
  teamRejectResponse;
}

@JsonEnum()
enum TeamListenerType {
  @JsonValue("TEAMINFO")
  teamInfo,
  @JsonValue("TEAM_JOIN_REQUESTS")
  teamJoinRequests,
  @JsonValue("TEAM_REQUEST_RESPONSES")
  teamRequestResponses;
}

@JsonEnum()
enum TeamErrorMessage {
  @JsonValue("INVALID_REQUEST")
  invalidRequest,
  @JsonValue("INVALID_TOKEN")
  invalidToken,
  @JsonValue("UPGRADE_API_VERSION")
  upgradeApiVersion,
  @JsonValue("INVALID_API_VERSION")
  invalidApiVersion,
  @JsonValue("TOO_MANY_CONNECTIONS")
  tooManyConnections;
}

@JsonEnum()
enum TeamInitRole {
  @JsonValue("TEAM_LEADER")
  teamLeader,
  @JsonValue("TEAM_JOINER")
  teamJoiner;
}

sealed class RequestMessageBase {
  String get type;

  static RequestMessageBase fromJson(Map<String, dynamic> json) {
    switch (json['type']) {
      case 'init':
        return InitRequestMessage.fromJson(json);
      default:
        throw Exception('Unknown message type');
    }
  }

  Map<String, dynamic> toJson();

  const RequestMessageBase();
}

@JsonSerializable()
class InitRequestMessage extends RequestMessageBase {
  @override
  final String type = 'init';
  final String teamId;
  final String authToken;
  final TeamInitRole role;
  final List<String> protocolExtensions;

  const InitRequestMessage({
    required this.teamId,
    required this.authToken,
    required this.role,
    this.protocolExtensions = const [],
  });

  factory InitRequestMessage.fromJson(Map<String, dynamic> json) => _$InitRequestMessageFromJson(json);

  @override
  Map<String, dynamic> toJson() => _$InitRequestMessageToJson(this);
}

@JsonSerializable(createFactory: true)
class InitResponseMessage extends ResponseMessageBase{
  @override
  final String type = 'initResponse';
  final bool success;
  final TeamErrorMessage? errorMessage;

  const InitResponseMessage({
    required this.success,
    this.errorMessage
  });

  factory InitResponseMessage.fromJson(Map<String, dynamic> json) => _$InitResponseMessageFromJson(json);

  @override
  Map<String, dynamic> toJson() => _$InitResponseMessageToJson(this);
}

@immutable
sealed class ResponseMessageBase {
  String get type;

  static ResponseMessageBase fromJson(Map<String, dynamic> json) {
    switch (json['type']) {
      case 'initResponse':
        return InitResponseMessage.fromJson(json);
      case 'teamJoinRequest':
        return TeamJoinRequestMessage.fromJson(json);
      default:
        throw Exception('Unknown message type');
    }
  }

  Map<String, dynamic> toJson();

  const ResponseMessageBase();
}

@JsonSerializable(createFactory: true)
class TeamJoinRequestMessage extends ResponseMessageBase {
  @override
  final String type = 'teamJoinRequest';
  final String teamId;
  final String userId;

  const TeamJoinRequestMessage({
    required this.teamId,
    required this.userId
  });

  factory TeamJoinRequestMessage.fromJson(Map<String, dynamic> json) => _$TeamJoinRequestMessageFromJson(json);

  @override
  Map<String, dynamic> toJson() => _$TeamJoinRequestMessageToJson(this);
}