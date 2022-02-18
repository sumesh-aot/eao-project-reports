from urllib import response
from flask import current_app

from reports_api.models import Project, project


class ProjectService:
    """Service to manage project related operations."""

    @classmethod
    def find(cls, project_id):
        return Project.find_by_id(project_id).as_dict()

    @classmethod
    def find_all(cls):
        """Find all projects"""
        response = {'projects': []}
        for row in Project.find_all():
            response['projects'].append(row.as_dict())
        return response

    @classmethod
    def create_project(cls, payload: dict):
        project = Project(**payload)
        current_app.logger.info(f'Project obj {dir(project)}')
        project.save()
        return project

    @classmethod
    def update_project(cls, project_id: int, payload: dict):
        project = Project.find_by_id(project_id)
        project = project.update(payload)
        return project

    @classmethod
    def delete_project(cls, project_id: int):
        project = Project.find_by_id(project_id)
        project.delete()
        return True
