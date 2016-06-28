// Generated by the gRPC protobuf plugin.
// If you make any local change, they will be lost.
// source: underworlds.proto

#include "underworlds.pb.h"
#include "underworlds.grpc.pb.h"

#include <grpc++/impl/codegen/async_stream.h>
#include <grpc++/impl/codegen/async_unary_call.h>
#include <grpc++/impl/codegen/channel_interface.h>
#include <grpc++/impl/codegen/client_unary_call.h>
#include <grpc++/impl/codegen/method_handler_impl.h>
#include <grpc++/impl/codegen/rpc_service_method.h>
#include <grpc++/impl/codegen/service_type.h>
#include <grpc++/impl/codegen/sync_stream.h>
namespace underworlds {

static const char* Underworlds_method_names[] = {
  "/underworlds.Underworlds/helo",
  "/underworlds.Underworlds/uptime",
  "/underworlds.Underworlds/topology",
  "/underworlds.Underworlds/getNodesLen",
  "/underworlds.Underworlds/getNodesIds",
  "/underworlds.Underworlds/getRootNode",
  "/underworlds.Underworlds/getNode",
  "/underworlds.Underworlds/updateNode",
  "/underworlds.Underworlds/deleteNode",
  "/underworlds.Underworlds/getNodeInvalidations",
  "/underworlds.Underworlds/timelineOrigin",
  "/underworlds.Underworlds/event",
  "/underworlds.Underworlds/startSituation",
  "/underworlds.Underworlds/endSituation",
  "/underworlds.Underworlds/getTimelineInvalidations",
  "/underworlds.Underworlds/hasMesh",
  "/underworlds.Underworlds/getMesh",
  "/underworlds.Underworlds/pushMesh",
};

std::unique_ptr< Underworlds::Stub> Underworlds::NewStub(const std::shared_ptr< ::grpc::ChannelInterface>& channel, const ::grpc::StubOptions& options) {
  std::unique_ptr< Underworlds::Stub> stub(new Underworlds::Stub(channel));
  return stub;
}

Underworlds::Stub::Stub(const std::shared_ptr< ::grpc::ChannelInterface>& channel)
  : channel_(channel), rpcmethod_helo_(Underworlds_method_names[0], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_uptime_(Underworlds_method_names[1], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_topology_(Underworlds_method_names[2], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_getNodesLen_(Underworlds_method_names[3], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_getNodesIds_(Underworlds_method_names[4], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_getRootNode_(Underworlds_method_names[5], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_getNode_(Underworlds_method_names[6], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_updateNode_(Underworlds_method_names[7], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_deleteNode_(Underworlds_method_names[8], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_getNodeInvalidations_(Underworlds_method_names[9], ::grpc::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_timelineOrigin_(Underworlds_method_names[10], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_event_(Underworlds_method_names[11], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_startSituation_(Underworlds_method_names[12], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_endSituation_(Underworlds_method_names[13], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_getTimelineInvalidations_(Underworlds_method_names[14], ::grpc::RpcMethod::SERVER_STREAMING, channel)
  , rpcmethod_hasMesh_(Underworlds_method_names[15], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_getMesh_(Underworlds_method_names[16], ::grpc::RpcMethod::NORMAL_RPC, channel)
  , rpcmethod_pushMesh_(Underworlds_method_names[17], ::grpc::RpcMethod::NORMAL_RPC, channel)
  {}

::grpc::Status Underworlds::Stub::helo(::grpc::ClientContext* context, const ::underworlds::Name& request, ::underworlds::Client* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_helo_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Client>* Underworlds::Stub::AsyncheloRaw(::grpc::ClientContext* context, const ::underworlds::Name& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Client>(channel_.get(), cq, rpcmethod_helo_, context, request);
}

::grpc::Status Underworlds::Stub::uptime(::grpc::ClientContext* context, const ::underworlds::Client& request, ::underworlds::Time* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_uptime_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Time>* Underworlds::Stub::AsyncuptimeRaw(::grpc::ClientContext* context, const ::underworlds::Client& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Time>(channel_.get(), cq, rpcmethod_uptime_, context, request);
}

::grpc::Status Underworlds::Stub::topology(::grpc::ClientContext* context, const ::underworlds::Client& request, ::underworlds::Topology* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_topology_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Topology>* Underworlds::Stub::AsynctopologyRaw(::grpc::ClientContext* context, const ::underworlds::Client& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Topology>(channel_.get(), cq, rpcmethod_topology_, context, request);
}

::grpc::Status Underworlds::Stub::getNodesLen(::grpc::ClientContext* context, const ::underworlds::Context& request, ::underworlds::Size* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_getNodesLen_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Size>* Underworlds::Stub::AsyncgetNodesLenRaw(::grpc::ClientContext* context, const ::underworlds::Context& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Size>(channel_.get(), cq, rpcmethod_getNodesLen_, context, request);
}

::grpc::Status Underworlds::Stub::getNodesIds(::grpc::ClientContext* context, const ::underworlds::Context& request, ::underworlds::Nodes* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_getNodesIds_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Nodes>* Underworlds::Stub::AsyncgetNodesIdsRaw(::grpc::ClientContext* context, const ::underworlds::Context& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Nodes>(channel_.get(), cq, rpcmethod_getNodesIds_, context, request);
}

::grpc::Status Underworlds::Stub::getRootNode(::grpc::ClientContext* context, const ::underworlds::Context& request, ::underworlds::Node* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_getRootNode_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Node>* Underworlds::Stub::AsyncgetRootNodeRaw(::grpc::ClientContext* context, const ::underworlds::Context& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Node>(channel_.get(), cq, rpcmethod_getRootNode_, context, request);
}

::grpc::Status Underworlds::Stub::getNode(::grpc::ClientContext* context, const ::underworlds::NodeInContext& request, ::underworlds::Node* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_getNode_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Node>* Underworlds::Stub::AsyncgetNodeRaw(::grpc::ClientContext* context, const ::underworlds::NodeInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Node>(channel_.get(), cq, rpcmethod_getNode_, context, request);
}

::grpc::Status Underworlds::Stub::updateNode(::grpc::ClientContext* context, const ::underworlds::NodeInContext& request, ::underworlds::Empty* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_updateNode_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Empty>* Underworlds::Stub::AsyncupdateNodeRaw(::grpc::ClientContext* context, const ::underworlds::NodeInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Empty>(channel_.get(), cq, rpcmethod_updateNode_, context, request);
}

::grpc::Status Underworlds::Stub::deleteNode(::grpc::ClientContext* context, const ::underworlds::NodeInContext& request, ::underworlds::Empty* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_deleteNode_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Empty>* Underworlds::Stub::AsyncdeleteNodeRaw(::grpc::ClientContext* context, const ::underworlds::NodeInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Empty>(channel_.get(), cq, rpcmethod_deleteNode_, context, request);
}

::grpc::ClientReader< ::underworlds::NodeInvalidation>* Underworlds::Stub::getNodeInvalidationsRaw(::grpc::ClientContext* context, const ::underworlds::Context& request) {
  return new ::grpc::ClientReader< ::underworlds::NodeInvalidation>(channel_.get(), rpcmethod_getNodeInvalidations_, context, request);
}

::grpc::ClientAsyncReader< ::underworlds::NodeInvalidation>* Underworlds::Stub::AsyncgetNodeInvalidationsRaw(::grpc::ClientContext* context, const ::underworlds::Context& request, ::grpc::CompletionQueue* cq, void* tag) {
  return new ::grpc::ClientAsyncReader< ::underworlds::NodeInvalidation>(channel_.get(), cq, rpcmethod_getNodeInvalidations_, context, request, tag);
}

::grpc::Status Underworlds::Stub::timelineOrigin(::grpc::ClientContext* context, const ::underworlds::Context& request, ::underworlds::Time* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_timelineOrigin_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Time>* Underworlds::Stub::AsynctimelineOriginRaw(::grpc::ClientContext* context, const ::underworlds::Context& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Time>(channel_.get(), cq, rpcmethod_timelineOrigin_, context, request);
}

::grpc::Status Underworlds::Stub::event(::grpc::ClientContext* context, const ::underworlds::SituationInContext& request, ::underworlds::Empty* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_event_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Empty>* Underworlds::Stub::AsynceventRaw(::grpc::ClientContext* context, const ::underworlds::SituationInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Empty>(channel_.get(), cq, rpcmethod_event_, context, request);
}

::grpc::Status Underworlds::Stub::startSituation(::grpc::ClientContext* context, const ::underworlds::SituationInContext& request, ::underworlds::Empty* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_startSituation_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Empty>* Underworlds::Stub::AsyncstartSituationRaw(::grpc::ClientContext* context, const ::underworlds::SituationInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Empty>(channel_.get(), cq, rpcmethod_startSituation_, context, request);
}

::grpc::Status Underworlds::Stub::endSituation(::grpc::ClientContext* context, const ::underworlds::SituationInContext& request, ::underworlds::Empty* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_endSituation_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Empty>* Underworlds::Stub::AsyncendSituationRaw(::grpc::ClientContext* context, const ::underworlds::SituationInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Empty>(channel_.get(), cq, rpcmethod_endSituation_, context, request);
}

::grpc::ClientReader< ::underworlds::TimelineInvalidation>* Underworlds::Stub::getTimelineInvalidationsRaw(::grpc::ClientContext* context, const ::underworlds::Context& request) {
  return new ::grpc::ClientReader< ::underworlds::TimelineInvalidation>(channel_.get(), rpcmethod_getTimelineInvalidations_, context, request);
}

::grpc::ClientAsyncReader< ::underworlds::TimelineInvalidation>* Underworlds::Stub::AsyncgetTimelineInvalidationsRaw(::grpc::ClientContext* context, const ::underworlds::Context& request, ::grpc::CompletionQueue* cq, void* tag) {
  return new ::grpc::ClientAsyncReader< ::underworlds::TimelineInvalidation>(channel_.get(), cq, rpcmethod_getTimelineInvalidations_, context, request, tag);
}

::grpc::Status Underworlds::Stub::hasMesh(::grpc::ClientContext* context, const ::underworlds::MeshInContext& request, ::underworlds::Bool* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_hasMesh_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Bool>* Underworlds::Stub::AsynchasMeshRaw(::grpc::ClientContext* context, const ::underworlds::MeshInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Bool>(channel_.get(), cq, rpcmethod_hasMesh_, context, request);
}

::grpc::Status Underworlds::Stub::getMesh(::grpc::ClientContext* context, const ::underworlds::MeshInContext& request, ::underworlds::Mesh* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_getMesh_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Mesh>* Underworlds::Stub::AsyncgetMeshRaw(::grpc::ClientContext* context, const ::underworlds::MeshInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Mesh>(channel_.get(), cq, rpcmethod_getMesh_, context, request);
}

::grpc::Status Underworlds::Stub::pushMesh(::grpc::ClientContext* context, const ::underworlds::MeshInContext& request, ::underworlds::Empty* response) {
  return ::grpc::BlockingUnaryCall(channel_.get(), rpcmethod_pushMesh_, context, request, response);
}

::grpc::ClientAsyncResponseReader< ::underworlds::Empty>* Underworlds::Stub::AsyncpushMeshRaw(::grpc::ClientContext* context, const ::underworlds::MeshInContext& request, ::grpc::CompletionQueue* cq) {
  return new ::grpc::ClientAsyncResponseReader< ::underworlds::Empty>(channel_.get(), cq, rpcmethod_pushMesh_, context, request);
}

Underworlds::Service::Service() {
  (void)Underworlds_method_names;
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[0],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::Name, ::underworlds::Client>(
          std::mem_fn(&Underworlds::Service::helo), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[1],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::Client, ::underworlds::Time>(
          std::mem_fn(&Underworlds::Service::uptime), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[2],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::Client, ::underworlds::Topology>(
          std::mem_fn(&Underworlds::Service::topology), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[3],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::Context, ::underworlds::Size>(
          std::mem_fn(&Underworlds::Service::getNodesLen), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[4],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::Context, ::underworlds::Nodes>(
          std::mem_fn(&Underworlds::Service::getNodesIds), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[5],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::Context, ::underworlds::Node>(
          std::mem_fn(&Underworlds::Service::getRootNode), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[6],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::NodeInContext, ::underworlds::Node>(
          std::mem_fn(&Underworlds::Service::getNode), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[7],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::NodeInContext, ::underworlds::Empty>(
          std::mem_fn(&Underworlds::Service::updateNode), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[8],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::NodeInContext, ::underworlds::Empty>(
          std::mem_fn(&Underworlds::Service::deleteNode), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[9],
      ::grpc::RpcMethod::SERVER_STREAMING,
      new ::grpc::ServerStreamingHandler< Underworlds::Service, ::underworlds::Context, ::underworlds::NodeInvalidation>(
          std::mem_fn(&Underworlds::Service::getNodeInvalidations), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[10],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::Context, ::underworlds::Time>(
          std::mem_fn(&Underworlds::Service::timelineOrigin), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[11],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::SituationInContext, ::underworlds::Empty>(
          std::mem_fn(&Underworlds::Service::event), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[12],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::SituationInContext, ::underworlds::Empty>(
          std::mem_fn(&Underworlds::Service::startSituation), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[13],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::SituationInContext, ::underworlds::Empty>(
          std::mem_fn(&Underworlds::Service::endSituation), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[14],
      ::grpc::RpcMethod::SERVER_STREAMING,
      new ::grpc::ServerStreamingHandler< Underworlds::Service, ::underworlds::Context, ::underworlds::TimelineInvalidation>(
          std::mem_fn(&Underworlds::Service::getTimelineInvalidations), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[15],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::MeshInContext, ::underworlds::Bool>(
          std::mem_fn(&Underworlds::Service::hasMesh), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[16],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::MeshInContext, ::underworlds::Mesh>(
          std::mem_fn(&Underworlds::Service::getMesh), this)));
  AddMethod(new ::grpc::RpcServiceMethod(
      Underworlds_method_names[17],
      ::grpc::RpcMethod::NORMAL_RPC,
      new ::grpc::RpcMethodHandler< Underworlds::Service, ::underworlds::MeshInContext, ::underworlds::Empty>(
          std::mem_fn(&Underworlds::Service::pushMesh), this)));
}

Underworlds::Service::~Service() {
}

::grpc::Status Underworlds::Service::helo(::grpc::ServerContext* context, const ::underworlds::Name* request, ::underworlds::Client* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::uptime(::grpc::ServerContext* context, const ::underworlds::Client* request, ::underworlds::Time* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::topology(::grpc::ServerContext* context, const ::underworlds::Client* request, ::underworlds::Topology* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::getNodesLen(::grpc::ServerContext* context, const ::underworlds::Context* request, ::underworlds::Size* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::getNodesIds(::grpc::ServerContext* context, const ::underworlds::Context* request, ::underworlds::Nodes* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::getRootNode(::grpc::ServerContext* context, const ::underworlds::Context* request, ::underworlds::Node* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::getNode(::grpc::ServerContext* context, const ::underworlds::NodeInContext* request, ::underworlds::Node* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::updateNode(::grpc::ServerContext* context, const ::underworlds::NodeInContext* request, ::underworlds::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::deleteNode(::grpc::ServerContext* context, const ::underworlds::NodeInContext* request, ::underworlds::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::getNodeInvalidations(::grpc::ServerContext* context, const ::underworlds::Context* request, ::grpc::ServerWriter< ::underworlds::NodeInvalidation>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::timelineOrigin(::grpc::ServerContext* context, const ::underworlds::Context* request, ::underworlds::Time* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::event(::grpc::ServerContext* context, const ::underworlds::SituationInContext* request, ::underworlds::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::startSituation(::grpc::ServerContext* context, const ::underworlds::SituationInContext* request, ::underworlds::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::endSituation(::grpc::ServerContext* context, const ::underworlds::SituationInContext* request, ::underworlds::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::getTimelineInvalidations(::grpc::ServerContext* context, const ::underworlds::Context* request, ::grpc::ServerWriter< ::underworlds::TimelineInvalidation>* writer) {
  (void) context;
  (void) request;
  (void) writer;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::hasMesh(::grpc::ServerContext* context, const ::underworlds::MeshInContext* request, ::underworlds::Bool* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::getMesh(::grpc::ServerContext* context, const ::underworlds::MeshInContext* request, ::underworlds::Mesh* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}

::grpc::Status Underworlds::Service::pushMesh(::grpc::ServerContext* context, const ::underworlds::MeshInContext* request, ::underworlds::Empty* response) {
  (void) context;
  (void) request;
  (void) response;
  return ::grpc::Status(::grpc::StatusCode::UNIMPLEMENTED, "");
}


}  // namespace underworlds
