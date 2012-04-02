from helper.app import create_app

app = create_app(__name__)

@app.context_processor
def inject_user():
    # note: At some point this could be placed in a helper module and passed to specific blueprints.
    from mu.model.domain.user import UserDomain

    user = UserDomain.user_of_session()
    if user:
        return dict(user=user.to_dict())
    return dict()

#        What would make this usable for me and others?
# @todo: Get Gravatar working as fallback. ;)
# @todo: Dropdown on the account button and boxed. Points to View Profile, Edit Account pages.
# @todo: ACL.
# @todo: Database design for how often I wish to be notified?
# ---
# @todo: Change the order of the mediums, statuses, types, etc.
# @todo: Add Release, Album, EP, etc. should alter the selected default.
# @todo: Valid time periods are stored inside a special class. Version. Validate against this, and use to store correctly.
# @todo: View/Edit Artist, View/Edit Release.
# @todo: Database design for some kind of tag/genre grouping of services and releases.
# @todo: Order new releases by modified event date.
# @todo: Bulk automation.
# @todo: Visualisation on the front page. How do I create useful categories for data?
# @todo: Never-ending list on New Releases page.
# @todo: last.fm or theechonest photo/synopsis for artists/releases.
# ---
# @todo: Voting is added. Popularity becomes a category.
# @todo: Work out how altering the event date mechanism will work.
# ---
# @todo: Design and implement searching mechanism.
# ---
# @todo: OAuth. Facebook Connect.
# @todo: RSS.
# @todo: Services.
# ---
# @todo: FIX THIS: Lazy loading is very slow if it happens over and over again.
# ---
# @todo: UX: Add, Edit, Remove, Browse, View, Filter. Admin Features? Navigation?

from helper.controller import register_controller_blueprints
# "import controller" calls initialise which runs some special code that
# automatically loads each of the python files inside the controller folder.
import controller as controllers

register_controller_blueprints(app, controllers)
