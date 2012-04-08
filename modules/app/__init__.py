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

# @todo: Reduce bullshit that's not needed -- yet!
# @todo: Simple, simple, simple.
# @todo: Songkick, last.fm or theechonest photo/synopsis for artists/releases.
# @todo: Bulk automation. What genres? A daemon?
# @todo: RSS.
# @todo: View/Edit Artist, View/Edit Release.
# @todo: FIX THIS: Lazy loading is very slow if it happens over and over again.
# @todo: Never-ending list on New Releases page.
#        Deploy on Heroku. Google Analytics. SEO. Etc.
# ---
#        What would make this usable for me and others?
# @todo: Database design for how often I wish to be notified?
#        (1) Realtime, (2) Once a week, (3) Once a month, (4) Once every 6 months, (5) Never.
# @todo: Valid time periods are stored inside a special class. Version. Validate against this, and use to store correctly.
#        Time categories:
#        Year
#        Year-Month
#        Month (assume year)
#        Year-Month-Day or Month-Day, etc.
#        TBA
#        Spring, Summer, Autumn, Winter
#        Later this year
#        Sometime in
#        Sometime later this year
#        First Quarter, Third Quarter
#        Imminent?
#        In production/In studio
#        Can I do textual analysis?
#        Question mark symbol should lower certainty.
#        to or a - in between two dates should create a range.
#        Remove other words.
#        Always assume future. If date is passed assume imminent but decrease certainty.
# @todo: Database design for some kind of tag/genre grouping of services and releases.
#        Classifier: classifier_id, classifier_type_id, name
#        ClassifierType: classifier_type_id, name
#        ServiceClassifier, ProductClassifier.
#        Check last.fm and theechonest for ideas on how we will be storing data...
#        Simplify!
# @todo: Work out how altering the event date mechanism will work.
#        When an UserEvent is added count the UserEvents against an event with the same hash, also order by certainty.
#        Order by most recently created!
#        Certainty reduced if number of hashes in period of time is not strong, use this for threshold.
#        On tipover point update the main event.
#        Check reddit algorithm for 'ratings'.
# @todo: Add in support for Services. Avoid abstracting details right now...
#        Add Service Form, repository, etc.
# ---
# @todo: View Profile, Edit Account pages.
# @todo: Switch to Flask-Login / invalidate sessions correctly. :)
# @todo: ACL.
# ---
# @todo: OAuth. Facebook Connect.
# ---
# @todo: Visualisation on the front page. How do I create useful categories for data?
# @todo: Order new releases by modified event date.
# @todo: Design and implement searching mechanism.
# @todo: Voting is added. Popularity becomes a category.
# @todo: UX: Add, Edit, Remove, Browse, View, Filter. Admin Features? Navigation?
# ---


from helper.controller import register_controller_blueprints
# "import controller" calls initialise which runs some special code that
# automatically loads each of the python files inside the controller folder.
import controller as controllers

register_controller_blueprints(app, controllers)
