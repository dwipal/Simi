# -*- coding: utf-8 -*-

<%inherit file="/base.mako" />

<form name="login" method="POST" action="login">

	<input type="hidden" name="next" value="${c.next}"/>
Enter Password: <input type="password" name="password" /> <br>
               <input type="submit" name="submit" value="Submit" />
</form>

