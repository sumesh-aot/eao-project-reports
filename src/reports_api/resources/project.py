"""Resource for project endpoints."""
from http import HTTPStatus
from flask import current_app

from flask_restx import Namespace, Resource, cors

from reports_api.services import ProjectService
from reports_api.utils.util import cors_preflight

from reports_api.models import Project


API = Namespace('projects', description='Projects')


@cors_preflight('GET')
@API.route('', methods=['GET', 'POST', 'OPTIONS'])
class Projects(Resource):
    """Endpoint resource to manage projects."""

    @staticmethod
    @cors.crossdomain(origin='*')
    def get():
        """Return all projects."""
        return ProjectService.find_all(), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    def post():
        """Create new project"""
        project = ProjectService.create_project(API.payload)
        return project.as_dict(), HTTPStatus.CREATED


@cors_preflight('GET')
@API.route('/<int:project_id>', methods=['GET', 'PUT', 'DELETE', 'OPTIONS'])
class Project(Resource):
    """Endpoint resource to manage a project."""

    @staticmethod
    @cors.crossdomain(origin='*')
    def get(project_id):
        """Return details of a project."""
        return ProjectService.find(project_id), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    def put(project_id):
        """Update and return a project."""
        project = ProjectService.update_project(project_id, API.payload)
        return project.as_dict(), HTTPStatus.OK

    @staticmethod
    @cors.crossdomain(origin='*')
    def delete(project_id):
        """Delete a project"""
        ProjectService.delete_project(project_id)
        return {"message": "Project successfully deleted"}, HTTPStatus.OK
