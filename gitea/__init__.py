# coding: utf-8

# flake8: noqa

"""
    Gitea API

    This documentation describes the Gitea API.  # noqa: E501

    OpenAPI spec version: 1.22.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from gitea.api.activitypub_api import ActivitypubApi
from gitea.api.admin_api import AdminApi
from gitea.api.issue_api import IssueApi
from gitea.api.miscellaneous_api import MiscellaneousApi
from gitea.api.notification_api import NotificationApi
from gitea.api.organization_api import OrganizationApi
from gitea.api.package_api import PackageApi
from gitea.api.repository_api import RepositoryApi
from gitea.api.settings_api import SettingsApi
from gitea.api.user_api import UserApi
# import ApiClient
from gitea.api_client import ApiClient
from gitea.configuration import Configuration
# import models into sdk package
from gitea.models.api_error import APIError
from gitea.models.access_token import AccessToken
from gitea.models.action_variable import ActionVariable
from gitea.models.activity import Activity
from gitea.models.activity_pub import ActivityPub
from gitea.models.add_collaborator_option import AddCollaboratorOption
from gitea.models.add_time_option import AddTimeOption
from gitea.models.annotated_tag import AnnotatedTag
from gitea.models.annotated_tag_object import AnnotatedTagObject
from gitea.models.attachment import Attachment
from gitea.models.badge import Badge
from gitea.models.branch import Branch
from gitea.models.branch_protection import BranchProtection
from gitea.models.change_file_operation import ChangeFileOperation
from gitea.models.change_files_options import ChangeFilesOptions
from gitea.models.changed_file import ChangedFile
from gitea.models.combined_status import CombinedStatus
from gitea.models.comment import Comment
from gitea.models.commit import Commit
from gitea.models.commit_affected_files import CommitAffectedFiles
from gitea.models.commit_date_options import CommitDateOptions
from gitea.models.commit_meta import CommitMeta
from gitea.models.commit_stats import CommitStats
from gitea.models.commit_status import CommitStatus
from gitea.models.commit_status_state import CommitStatusState
from gitea.models.commit_user import CommitUser
from gitea.models.compare import Compare
from gitea.models.contents_response import ContentsResponse
from gitea.models.create_access_token_option import CreateAccessTokenOption
from gitea.models.create_branch_protection_option import CreateBranchProtectionOption
from gitea.models.create_branch_repo_option import CreateBranchRepoOption
from gitea.models.create_email_option import CreateEmailOption
from gitea.models.create_file_options import CreateFileOptions
from gitea.models.create_fork_option import CreateForkOption
from gitea.models.create_gpg_key_option import CreateGPGKeyOption
from gitea.models.create_hook_option import CreateHookOption
from gitea.models.create_hook_option_config import CreateHookOptionConfig
from gitea.models.create_issue_comment_option import CreateIssueCommentOption
from gitea.models.create_issue_option import CreateIssueOption
from gitea.models.create_key_option import CreateKeyOption
from gitea.models.create_label_option import CreateLabelOption
from gitea.models.create_milestone_option import CreateMilestoneOption
from gitea.models.create_o_auth2_application_options import CreateOAuth2ApplicationOptions
from gitea.models.create_or_update_secret_option import CreateOrUpdateSecretOption
from gitea.models.create_org_option import CreateOrgOption
from gitea.models.create_pull_request_option import CreatePullRequestOption
from gitea.models.create_pull_review_comment import CreatePullReviewComment
from gitea.models.create_pull_review_options import CreatePullReviewOptions
from gitea.models.create_push_mirror_option import CreatePushMirrorOption
from gitea.models.create_release_option import CreateReleaseOption
from gitea.models.create_repo_option import CreateRepoOption
from gitea.models.create_status_option import CreateStatusOption
from gitea.models.create_tag_option import CreateTagOption
from gitea.models.create_team_option import CreateTeamOption
from gitea.models.create_user_option import CreateUserOption
from gitea.models.create_variable_option import CreateVariableOption
from gitea.models.create_wiki_page_options import CreateWikiPageOptions
from gitea.models.cron import Cron
from gitea.models.delete_email_option import DeleteEmailOption
from gitea.models.delete_file_options import DeleteFileOptions
from gitea.models.deploy_key import DeployKey
from gitea.models.dismiss_pull_review_options import DismissPullReviewOptions
from gitea.models.edit_attachment_options import EditAttachmentOptions
from gitea.models.edit_branch_protection_option import EditBranchProtectionOption
from gitea.models.edit_deadline_option import EditDeadlineOption
from gitea.models.edit_git_hook_option import EditGitHookOption
from gitea.models.edit_hook_option import EditHookOption
from gitea.models.edit_issue_comment_option import EditIssueCommentOption
from gitea.models.edit_issue_option import EditIssueOption
from gitea.models.edit_label_option import EditLabelOption
from gitea.models.edit_milestone_option import EditMilestoneOption
from gitea.models.edit_org_option import EditOrgOption
from gitea.models.edit_pull_request_option import EditPullRequestOption
from gitea.models.edit_reaction_option import EditReactionOption
from gitea.models.edit_release_option import EditReleaseOption
from gitea.models.edit_repo_option import EditRepoOption
from gitea.models.edit_team_option import EditTeamOption
from gitea.models.edit_user_option import EditUserOption
from gitea.models.email import Email
from gitea.models.external_tracker import ExternalTracker
from gitea.models.external_wiki import ExternalWiki
from gitea.models.file_commit_response import FileCommitResponse
from gitea.models.file_delete_response import FileDeleteResponse
from gitea.models.file_links_response import FileLinksResponse
from gitea.models.file_response import FileResponse
from gitea.models.files_response import FilesResponse
from gitea.models.gpg_key import GPGKey
from gitea.models.gpg_key_email import GPGKeyEmail
from gitea.models.general_api_settings import GeneralAPISettings
from gitea.models.general_attachment_settings import GeneralAttachmentSettings
from gitea.models.general_repo_settings import GeneralRepoSettings
from gitea.models.general_ui_settings import GeneralUISettings
from gitea.models.generate_repo_option import GenerateRepoOption
from gitea.models.git_blob_response import GitBlobResponse
from gitea.models.git_entry import GitEntry
from gitea.models.git_hook import GitHook
from gitea.models.git_object import GitObject
from gitea.models.git_tree_response import GitTreeResponse
from gitea.models.gitignore_template_info import GitignoreTemplateInfo
from gitea.models.hook import Hook
from gitea.models.id_assets_body import IdAssetsBody
from gitea.models.id_assets_body1 import IdAssetsBody1
from gitea.models.id_assets_body2 import IdAssetsBody2
from gitea.models.identity import Identity
from gitea.models.index_assets_body import IndexAssetsBody
from gitea.models.inline_response200 import InlineResponse200
from gitea.models.inline_response2001 import InlineResponse2001
from gitea.models.internal_tracker import InternalTracker
from gitea.models.issue import Issue
from gitea.models.issue_config import IssueConfig
from gitea.models.issue_config_contact_link import IssueConfigContactLink
from gitea.models.issue_config_validation import IssueConfigValidation
from gitea.models.issue_deadline import IssueDeadline
from gitea.models.issue_form_field import IssueFormField
from gitea.models.issue_form_field_type import IssueFormFieldType
from gitea.models.issue_form_field_visible import IssueFormFieldVisible
from gitea.models.issue_labels_option import IssueLabelsOption
from gitea.models.issue_meta import IssueMeta
from gitea.models.issue_template import IssueTemplate
from gitea.models.issue_template_labels import IssueTemplateLabels
from gitea.models.label import Label
from gitea.models.label_template import LabelTemplate
from gitea.models.license_template_info import LicenseTemplateInfo
from gitea.models.licenses_template_list_entry import LicensesTemplateListEntry
from gitea.models.markdown_option import MarkdownOption
from gitea.models.markup_option import MarkupOption
from gitea.models.merge_pull_request_option import MergePullRequestOption
from gitea.models.migrate_repo_options import MigrateRepoOptions
from gitea.models.milestone import Milestone
from gitea.models.new_issue_pins_allowed import NewIssuePinsAllowed
from gitea.models.node_info import NodeInfo
from gitea.models.node_info_services import NodeInfoServices
from gitea.models.node_info_software import NodeInfoSoftware
from gitea.models.node_info_usage import NodeInfoUsage
from gitea.models.node_info_usage_users import NodeInfoUsageUsers
from gitea.models.note import Note
from gitea.models.notification_count import NotificationCount
from gitea.models.notification_subject import NotificationSubject
from gitea.models.notification_thread import NotificationThread
from gitea.models.notify_subject_type import NotifySubjectType
from gitea.models.o_auth2_application import OAuth2Application
from gitea.models.organization import Organization
from gitea.models.organization_permissions import OrganizationPermissions
from gitea.models.pr_branch_info import PRBranchInfo
from gitea.models.package import Package
from gitea.models.package_file import PackageFile
from gitea.models.payload_commit import PayloadCommit
from gitea.models.payload_commit_verification import PayloadCommitVerification
from gitea.models.payload_user import PayloadUser
from gitea.models.permission import Permission
from gitea.models.public_key import PublicKey
from gitea.models.pull_request import PullRequest
from gitea.models.pull_request_meta import PullRequestMeta
from gitea.models.pull_review import PullReview
from gitea.models.pull_review_comment import PullReviewComment
from gitea.models.pull_review_request_options import PullReviewRequestOptions
from gitea.models.push_mirror import PushMirror
from gitea.models.reaction import Reaction
from gitea.models.reference import Reference
from gitea.models.release import Release
from gitea.models.rename_user_option import RenameUserOption
from gitea.models.repo_collaborator_permission import RepoCollaboratorPermission
from gitea.models.repo_commit import RepoCommit
from gitea.models.repo_topic_options import RepoTopicOptions
from gitea.models.repo_transfer import RepoTransfer
from gitea.models.repository import Repository
from gitea.models.repository_meta import RepositoryMeta
from gitea.models.review_state_type import ReviewStateType
from gitea.models.search_results import SearchResults
from gitea.models.secret import Secret
from gitea.models.server_version import ServerVersion
from gitea.models.state_type import StateType
from gitea.models.stop_watch import StopWatch
from gitea.models.submit_pull_review_options import SubmitPullReviewOptions
from gitea.models.tag import Tag
from gitea.models.team import Team
from gitea.models.time_stamp import TimeStamp
from gitea.models.timeline_comment import TimelineComment
from gitea.models.topic_name import TopicName
from gitea.models.topic_response import TopicResponse
from gitea.models.tracked_time import TrackedTime
from gitea.models.transfer_repo_option import TransferRepoOption
from gitea.models.update_file_options import UpdateFileOptions
from gitea.models.update_repo_avatar_option import UpdateRepoAvatarOption
from gitea.models.update_user_avatar_option import UpdateUserAvatarOption
from gitea.models.update_variable_option import UpdateVariableOption
from gitea.models.user import User
from gitea.models.user_badge_option import UserBadgeOption
from gitea.models.user_heatmap_data import UserHeatmapData
from gitea.models.user_settings import UserSettings
from gitea.models.user_settings_options import UserSettingsOptions
from gitea.models.watch_info import WatchInfo
from gitea.models.wiki_commit import WikiCommit
from gitea.models.wiki_commit_list import WikiCommitList
from gitea.models.wiki_page import WikiPage
from gitea.models.wiki_page_meta_data import WikiPageMetaData
